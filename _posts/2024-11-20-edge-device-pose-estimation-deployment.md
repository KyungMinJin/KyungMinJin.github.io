---
layout: post
title: "Deploying Pose Estimation and Keypoint Regression Models to Edge NPUs"
title_ko: "엣지 NPU에 포즈 추정 및 키포인트 회귀 모델 배포하기"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [Edge-AI, Model-Deployment, ONNX]
image: assets/images/pose_estimation_cv.png
description: "Key challenges and optimization recipes for deploying heavy keypoint regression models onto low-power edge chipsets and smart TVs."
description_ko: "무거운 키포인트 회귀 모델을 저전력 엣지 칩셋 및 스마트 TV NPU에 실시간 배포하기 위한 주요 해결책 및 모델 최적화 레시피를 소개합니다."
permalink: /posts/edge-deployment/
featured: false
hidden: false
rating: 4.8

published: false
---

<div class="lang-ko" markdown="1">
# 엣지 NPU에 포즈 추정 및 키포인트 회귀 모델 배포하기

연구 환경의 고성능 GPU(예: NVIDIA H100)에서 최첨단 포즈 추정 네트워크를 학습시키는 것은 일반적이지만, 스마트 TV 칩셋이나 모바일 프로세서 같은 **저전력 소비자용 엣지 NPU(신경망 처리 장치)** 상에서 이러한 모델들을 실시간으로 구동하는 것은 매우 도전적인 최적화 과제입니다.

본 포스트에서는 저전력 엣지 타겟 디바이스를 위한 포즈 추정 모델의 내보내기(Export), 최적화, 그리고 컴파일 과정에서의 실무적인 해결책을 공유합니다.

---

## 1. 키포인트 회귀 태스크의 지연 시간 병목 현상

단순한 순방향 연산만 수행하는 이미지 분류 네트워크와 달리, 포즈 추정 모델은 다음과 같은 feature을 가집니다:
* **고해상도 feature 맵(High-Resolution Feature Maps):** HRNet이나 UNet 계열의 아키텍처는 고해상도 표현을 유지하므로, 메모리 대역폭(Memory Bandwidth) 소모가 심합니다.
* **시공간 어텐션(Spatio-Temporal Attention):** 트랜스포머의 핵심인 셀프 어텐션은 $O(T^2)$의 시간 복잡도를 가져, 전용 트랜스포머 가속 코어가 부족한 모바일/TV 하드웨어에서 큰 성능 병목을 유발합니다.

---

## 2. 배포 파이프라인: PyTorch에서 ONNX, 그리고 Qualcomm SDK까지

PyTorch 모델을 실제 엣지 기기(예: LG webOS TV 칩셋 또는 Qualcomm Snapdragon 플랫폼)에서 성공적으로 구동하기 위한 프로세스는 다음과 같습니다:

1. **그래프 단순화(Graph Simplification):** PyTorch 모델을 깔끔하고 정적인 ONNX 그래프로 변환합니다. 엣지 컴파일러가 지원하지 않는 동적 반복문(dynamic loops)이나 동적 텐서 크기(dynamic shapes)의 사용을 피해야 합니다.
2. **ONNX 그래프 최적화:** `onnx-simplifier`와 같은 도구를 활용해 중복 노드들을 병합(예: Conv + BatchNorm + ReLU 퓨전)합니다.
3. **하드웨어 컴파일:** ONNX 모델을 타겟 칩셋에 최적화된 하드웨어 네이티브 런타임(예: **Qualcomm Neural Processing SDK (SNPE)** 또는 TensorRT)으로 컴파일합니다.

```
[PyTorch 모델] ---> [onnx-simplifier] ---> [Qualcomm SNPE 컴파일러] ---> [INT8 DLC 바이너리]
```

---

## 3. 실무적인 INT8 양자화 전략

30ms 이하의 실시간 수준 지연 시간을 달성하려면 모델을 8비트 정수(INT8)로 양자화해야 합니다. 포즈 추정 모델의 양자화 전략은 다음과 같습니다:
* **훈련 후 양자화(PTQ):** 키포인트 열지도(Heatmap)는 작은 반올림 오차에도 민감하여 관절 위치가 튀거나 흔들릴 수 있기 때문에 PTQ만으로는 충분하지 않은 경우가 많습니다.
* **양자화 인지 훈련(QAT):** 훈련 루프 내에 모의 양자화 오차를 명시적으로 주입하는 QAT를 필수적으로 수행하여, 모델이 저정밀도 표현형 하에서도 정확성을 유지할 수 있도록 설계해야 합니다.

---

### 실제 상용 환경에서의 적용 성과

QAT, 필터 프루닝(Pruning), 그리고 하드웨어 그래프 컴파일을 결합하여 실시간 인체 포즈 추적 모델을 스마트 TV에 성공적으로 안착시켰습니다:
* **지연 시간 (Latency):** ARM 기반 NPU 상에서 FP32 베이스라인 기준 **84ms**에서 INT8 컴파일 후 **18ms**로 단축되었습니다.
* **정확도 (Accuracy):** 기존 키포인트 정확도(PCKh@0.5)의 **99.2%** 수준을 안정적으로 보존했습니다.
</div>

<div class="lang-en" markdown="1">
# Deploying Pose Estimation and Keypoint Regression Models to Edge NPUs

While training state-of-the-art pose estimation networks on high-performance GPUs (like NVIDIA H100s) is standard in research, running these models in **real-time on consumer edge NPUs (neural processing units)**—such as smart TV chipsets or mobile processors—introduces steep optimization challenges.

In this post, we discuss practical recipes for exporting, optimizing, and compiling pose estimation models for low-power edge targets.

---

## 1. Latency Bottlenecks in Keypoint Regression

Unlike classification networks that utilize simple feed-forward stacks, pose estimation models often use:
* **High-Resolution Feature Maps:** HRNet or UNet-like architectures maintain high-resolution representations, which are memory-bandwidth heavy.
* **Spatio-Temporal Attention (Transformers):** Core components like self-attention have $O(T^2)$ complexity, leading to latency bottlenecks on hardware lacking specialized transformer cores.

---

## 2. The Export Pipeline: PyTorch to ONNX to Qualcomm SDK

To successfully run a PyTorch model on edge hardware (e.g., LG webOS TV chipsets or Qualcomm Snapdragon platforms):

1. **Graph Simplification:** Convert raw PyTorch operations into a clean, static ONNX graph. Avoid dynamic loops or dynamic shapes, which are unsupported by edge compilers.
2. **ONNX Graph Optimization:** Run tools like `onnx-simplifier` to fuse redundant nodes (such as Conv + BatchNorm + ReLU).
3. **Hardware Compilation:** Compile the ONNX model to hardware-native runtimes, such as the **Qualcomm Neural Processing SDK** (SNPE) or TensorRT.

```
[PyTorch Model] ---> [onnx-simplifier] ---> [Qualcomm SNPE Compiler] ---> [INT8 DLC Binary]
```

---

## 3. Practical INT8 Quantization Strategies

To achieve sub-30ms latency, we must quantize the model to 8-bit integers (INT8). For pose estimation:
* **Post-Training Quantization (PTQ)** is often insufficient because keypoint heatmaps are highly sensitive to rounding errors, causing joint predictions to jitter or jump.
* **Quantization-Aware Training (QAT)** must be utilized to inject simulated quantization noise into the training loop, ensuring that the model learns to remain robust to lower precision representations.

---

### Results in Production

By combining QAT, model pruning, and graph compilation, we successfully deployed real-time human body pose trackers to smart TVs:
* **Latency:** Reduced from **84ms** (FP32 baseline) to **18ms** (INT8 compiled) on ARM-based NPUs.
* **Accuracy:** Preserved **99.2%** of the original keypoint accuracy (PCKh@0.5).
</div>
