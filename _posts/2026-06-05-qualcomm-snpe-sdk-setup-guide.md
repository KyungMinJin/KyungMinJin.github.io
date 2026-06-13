---
layout: post
title: "Practical Guide: Compiling and Deploying DL Models using Qualcomm SNPE SDK"
title_ko: "Qualcomm SNPE SDK를 활용한 딥러닝 모델 컴파일 및 배포 가이드"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [Edge-AI, Model-Deployment, SNPE, Deep-Learning]
image: assets/images/qat_pose_estimation.png
description: "A step-by-step developer tutorial on setting up the Qualcomm SNPE SDK, converting ONNX models to DLC, and running quantization-aware INT8 inference on Snapdragon NPUs."
description_ko: "Qualcomm SNPE SDK 환경 설정부터 ONNX 모델의 DLC 변환, INT8 양자화 및 C++ API 기반 추정 구동 방법까지 실제 엣지 디바이스 배포를 위한 가이드를 제공합니다."
permalink: /posts/snpe-setup-guide/
featured: false
hidden: false
rating: 4.8

published: false
---

<div class="lang-ko" markdown="1">
# Qualcomm SNPE SDK를 활용한 딥러닝 모델 컴파일 및 배포 가이드

Qualcomm Snapdragon 신경망 처리 장치(NPU)가 탑재된 엣지 칩셋에 딥러닝 모델을 배포하기 위해서는 기존의 모델 그래프를 **DLC(Deep Learning Container)**라는 전용 바이너리 포맷으로 변환해야 합니다. **Qualcomm Neural Processing SDK**(구 SNPE)는 모델의 변환, 양자화 및 NPU 상에서의 실행을 지원하는 툴체인을 제공합니다.

본 실무 가이드에서는 SNPE 개발 환경 설정부터 ONNX 모델의 DLC 변환, 캘리브레이션 데이터를 활용한 INT8 양자화, 그리고 SNPE C++ API를 활용한 모델 추정 구동까지의 전 과정을 차근차근 다룹니다.

---

## 1. 개발 환경 구축 및 사전 요구사항

모델 컴파일러는 리눅스 서버(Ubuntu 20.04/22.04 권장) 환경에서 실행해야 합니다. Python 종속 라이브러리를 설치하고 SDK 및 Android NDK를 다운로드하여 준비합니다.

### 환경 변수 설정
SDK 도구들을 쉘 환경에 등록하기 위해 `~/.bashrc` 파일 등에 다음과 같은 환경 변수를 구성합니다:

```bash
export SNPE_ROOT=/path/to/snpe-sdk
export ANDROID_NDK_ROOT=/path/to/android-ndk-r25c

# Python 환경 설정 스크립트 실행
source $SNPE_ROOT/bin/envsetup.sh -o $ANDROID_NDK_ROOT
```

활성화된 가상 환경에 필요한 Python 패키지(`protobuf`, `onnx`, `numpy`)들이 정상 설치되어 있는지 확인합니다:
```bash
pip install onnx==1.14.0 protobuf==3.20.3 numpy==1.23.5
```

---

## 2. 모델 변환: ONNX에서 DLC로

변환을 진행하기 전에, ONNX 그래프를 단순화(simplify)하여 지원되지 않는 연산자나 불필요한 노드(예: 융합되지 않은 Batch Normalization 레이어)를 미리 정리해 줍니다:

```bash
onnxsim input_model.onnx simplified_model.onnx
```

그 다음, `snpe-onnx-to-dlc` 컴파일러를 사용하여 단순화된 ONNX 파일을 `.dlc` 컨테이너 파일로 컴파일합니다. 이때 PyTorch 내보내기 시 설정했던 입력 텐서의 이름과 크기를 정확히 지정해주어야 합니다:

```bash
snpe-onnx-to-dlc \
  -i simplified_model.onnx \
  -d input_name "1,3,256,256" \
  -o model.dlc
```

* `-i`: 입력할 ONNX 그래프 경로.
* `-d`: 모델의 진입점 레이어 이름 및 텐서 차원 설정.
* `-o`: 출력될 비양자화 FP32 DLC 바이너리 경로.

---

## 3. INT8 양자화 및 캘리브레이션 (Calibration)

모델을 8비트 정수 정밀도(INT8)로 실행하면 엣지 NPU 상에서 **3~4배의 속도 향상**을 볼 수 있으며 메모리 대역폭 오버헤드도 크게 줄어듭니다. 포즈 추정 및 키포인트 회귀와 같이 미세한 수치 변화에 민감한 태스크의 정확도 하락을 예방하기 위해, 다음과 같이 훈련 후 캘리브레이션을 실행합니다:

### 캘리브레이션 데이터셋 준비
CHW 텐서 값이 저장된 약 100~200개의 원시 바이너리 플로트 파일(예: 이미지 픽셀 정보가 담긴 `.raw` 또는 `.bin` 파일)을 폴더에 모아 둔 후, 해당 파일들의 경로 목록이 적힌 `raw_list.txt`를 생성합니다:

```
# raw_list.txt
calibration_data/img_001.raw
calibration_data/img_002.raw
calibration_data/img_003.raw
```

### DLC 양자화 툴 실행
`snpe-dlc-quantize` 명령어를 사용하여 양자화 스케일 값을 DLC 컨테이너에 직접 삽입(bake)합니다:

```bash
snpe-dlc-quantize \
  --input_dlc model.dlc \
  --input_list raw_list.txt \
  --output_dlc model_quantized.dlc \
  --use_enhanced_quantizer
```

> [!TIP]
> `--use_enhanced_quantizer` 플래그를 추가하면 부동소수점 값과 양자화 값 간의 평균 제곱 오차(MSE)를 최소화하도록 양자화 스텝 크기를 최적화하는 알고리즘이 적용됩니다. 이는 키포인트가 흔들리는 현상을 억제하는 데 큰 도움이 됩니다.

---

## 4. C++ 추정 연동 (Inference Integration)

컴파일된 모델을 Android 혹은 임베디드 플랫폼 상에 통합하기 위해, SNPE API를 사용하여 DLC 컨테이너를 로드하고 추정을 수행하는 예제 코드입니다:

```cpp
#include "SNPE/SNPE.hpp"
#include "SNPE/SNPEBuilder.hpp"
#include "DlContainer/IDlContainer.hpp"

// 1. 양자화된 DLC 컨테이너 파일 로드
std::unique_ptr<zsnpe::IDlContainer> container = 
    zsnpe::IDlContainer::open("model_quantized.dlc");

// 2. 실행 대상 런타임 프로세서 선택 (NPU/DSP 선호, 차선책으로 CPU)
static zsnpe::Runtime_t runtime = zsnpe::Runtime_t::DSP;
if (!zsnpe::SNPEBuilder::isRuntimeAvailable(runtime)) {
    runtime = zsnpe::Runtime_t::CPU;
}

// 3. SNPE 실행 엔진 구축
zsnpe::SNPEBuilder snpeBuilder(container.get());
std::unique_ptr<zsnpe::SNPE> snpe = snpeBuilder
    .setOutputLayers({"output_name"})
    .setRuntimeProcessor(runtime)
    .build();

// 4. 입력 텐서 바인딩
zsnpe::TensorMap inputMap;
std::unique_ptr<zsnpe::ITensor> inputTensor = 
    snpeBuilder.getTensorBuilder().createTensor({1, 3, 256, 256});

// float 타입의 이미지 데이터를 inputTensor 버퍼로 복사...
// std::copy(image_data.begin(), image_data.end(), inputTensor->begin());
inputMap.add("input_name", inputTensor.get());

// 5. 추론 실행
zsnpe::TensorMap outputMap;
bool success = snpe->execute(inputMap, outputMap);

// 6. 출력 텐서로부터 예측값 획득
if (success) {
    zsnpe::ITensor* outputTensor = outputMap.getTensor("output_name");
    float* predictions = reinterpret_cast<float*>(outputTensor->begin().getBuffer());
    // 이곳에서 키포인트 히트맵 혹은 좌표 후처리 작업을 진행합니다.
}
```

---

## 5. 실무 디버깅 팁

* **텐서 차원 불일치 (Mismatched Dimensions):** 컴파일러에서 차원 오류가 발생하는 경우 ONNX 모델 내에 동적 크기(dynamic dimensions)가 남아있는지 체크하십시오. SNPE 컴파일러는 완전히 정적인(static) 입력 텐서 크기를 요구합니다.
* **정확도 급락 (Accuracy Drop):** 양자화 모델의 정확도가 급격히 하락하는 경우, 특정 레이어(예: 최종 좌표 회귀 레이어)는 FP16 정밀도로 예외 구동해야 할 수 있습니다. 양자화 시 `--override_params` 옵션을 사용하여 특정 레이어를 양자화 대상에서 제외할 수 있습니다.
* **QAT 모델 내보내기 (QAT Export):** PyTorch 환경에서 양자화 인지 훈련(QAT)을 완료했다면 ONNX opset 13 이상으로 모델을 내보내십시오. SNPE는 ONNX의 `QuantizeLinear`/`DequantizeLinear` 연산자를 하드웨어 전용 가속 명령어로 자동 매핑하므로 캘리브레이션 오차 문제를 예방할 수 있습니다.
</div>

<div class="lang-en" markdown="1">
# Practical Guide: Compiling and Deploying DL Models using Qualcomm SNPE SDK

Deploying deep learning models to edge chipsets equipped with Qualcomm Snapdragon Neural Processing Units (NPUs) requires converting standard model graphs into a proprietary binary format called **DLC (Deep Learning Container)**. The **Qualcomm Neural Processing SDK** (formerly SNPE) provides the toolchains necessary to convert, quantize, and execute models on target NPUs.

In this practical guide, we walk through setting up the SNPE development environment, converting an ONNX model to DLC, performing INT8 quantization with calibration data, and executing inference using the SNPE C++ API.

---

## 1. Environment Setup & Prerequisites

To compile models, you need a Linux development server (Ubuntu 20.04/22.04 is recommended). Prepare the environment by installing Python dependencies and downloading the SDK and Android NDK.

### Environment Variables
Configure your shell startup script (e.g., `~/.bashrc`) to register the SDK tools:

```bash
export SNPE_ROOT=/path/to/snpe-sdk
export ANDROID_NDK_ROOT=/path/to/android-ndk-r25c

# Setup Python environment
source $SNPE_ROOT/bin/envsetup.sh -o $ANDROID_NDK_ROOT
```

Ensure Python dependencies (`protobuf`, `onnx`, `numpy`) are installed in your active virtual environment:
```bash
pip install onnx==1.14.0 protobuf==3.20.3 numpy==1.23.5
```

---

## 2. Model Conversion: ONNX to DLC

Before converting, simplify your ONNX graph to resolve unsupported operations or redundant nodes (such as unfused Batch Normalization layers):

```bash
onnxsim input_model.onnx simplified_model.onnx
```

Next, use the `snpe-onnx-to-dlc` compiler to convert the simplified graph to a `.dlc` container. You must specify input shapes and names matching your PyTorch exporter variables:

```bash
snpe-onnx-to-dlc \
  -i simplified_model.onnx \
  -d input_name "1,3,256,256" \
  -o model.dlc
```

* `-i`: Path to the input ONNX graph.
* `-d`: Sets the layer name and dimension bounds for model entry points.
* `-o`: The output path for the unquantized FP32 DLC binary.

---

## 3. INT8 Quantization & Calibration

Running model execution at 8-bit integer precision (INT8) yields up to **3-4x latency speedups** and reduces memory bandwidth overhead on edge NPUs. To preserve accuracy in sensitive tasks like pose estimation and keypoint regression, we run post-training calibration:

### Prepare Calibration Dataset
Create a folder containing 100-200 representative inputs saved as raw binary float files (e.g., `.raw` or `.bin` files containing CHW tensor values). Then, create a `raw_list.txt` file listing their paths:

```
# raw_list.txt
calibration_data/img_001.raw
calibration_data/img_002.raw
calibration_data/img_003.raw
```

### Run DLC Quantizer
Run `snpe-dlc-quantize` to bake the quantization scales directly into the container:

```bash
snpe-dlc-quantize \
  --input_dlc model.dlc \
  --input_list raw_list.txt \
  --output_dlc model_quantized.dlc \
  --use_enhanced_quantizer
```

> [!TIP]
> Setting the `--use_enhanced_quantizer` flag uses an algorithm that adjusts the quantization step size to minimize Mean Squared Error (MSE) between float and quantized activations, which helps prevent keypoint jittering.

---

## 4. C++ Inference Integration

To integrate the compiled model on Android or embedded platforms, load the container and execute it using SNPE APIs:

```cpp
#include "SNPE/SNPE.hpp"
#include "SNPE/SNPEBuilder.hpp"
#include "DlContainer/IDlContainer.hpp"

// 1. Load the quantized DLC container
std::unique_ptr<zsnpe::IDlContainer> container = 
    zsnpe::IDlContainer::open("model_quantized.dlc");

// 2. Select target runtime (DSP / NPU takes priority, falls back to CPU)
static zsnpe::Runtime_t runtime = zsnpe::Runtime_t::DSP;
if (!zsnpe::SNPEBuilder::isRuntimeAvailable(runtime)) {
    runtime = zsnpe::Runtime_t::CPU;
}

// 3. Build the SNPE execution engine
zsnpe::SNPEBuilder snpeBuilder(container.get());
std::unique_ptr<zsnpe::SNPE> snpe = snpeBuilder
    .setOutputLayers({"output_name"})
    .setRuntimeProcessor(runtime)
    .build();

// 4. Bind Input Tensor
zsnpe::TensorMap inputMap;
std::unique_ptr<zsnpe::ITensor> inputTensor = 
    snpeBuilder.getTensorBuilder().createTensor({1, 3, 256, 256});

// Copy float image data to inputTensor buffer...
// std::copy(image_data.begin(), image_data.end(), inputTensor->begin());
inputMap.add("input_name", inputTensor.get());

// 5. Execute inference
zsnpe::TensorMap outputMap;
bool success = snpe->execute(inputMap, outputMap);

// 6. Retrieve predictions from output tensor
if (success) {
    zsnpe::ITensor* outputTensor = outputMap.getTensor("output_name");
    float* predictions = reinterpret_cast<float*>(outputTensor->begin().getBuffer());
    // Process keypoint heatmaps or coordinates here...
}
```

---

## 5. Practical Debugging Tips

* **Mismatched Dimensions:** If the compiler complains about shape errors, verify that ONNX dynamic dimensions are completely removed. SNPE compiler requires fully static input dimensions.
* **Accuracy Drop:** If the quantized model experiences severe accuracy degradation, evaluate if certain layers (e.g. final regression layers) need to run at FP16. You can exclude specific layers from quantization using the `--override_params` options during quantization.
* **QAT Export:** If you trained the model using Quantization-Aware Training (QAT) in PyTorch, export it using ONNX opset 13. SNPE will automatically map the `QuantizeLinear`/`DequantizeLinear` operators to native hardware instructions, avoiding calibration-based PTQ errors.
</div>
