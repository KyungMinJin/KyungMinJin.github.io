---
layout: post
title: "Quantization-Aware Training (QAT) for Edge Pose Estimation"
title_ko: "엣지 포즈 추정을 위한 양자화 인지 훈련 (Quantization-Aware Training, QAT)"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [Quantization, Edge-AI, Pose-Estimation]
image: assets/images/qat_pose_estimation.png
description: "How to use Quantization-Aware Training (QAT) to preserve keypoint accuracy when deploying pose estimation models to low-power edge hardware."
description_ko: "저전력 엣지 하드웨어에 포즈 추정 모델을 배포할 때, 양자화 인지 훈련(QAT)을 활용하여 키포인트 정확도 손실을 방지하고 성능을 가속화하는 방법을 설명합니다."
permalink: /posts/qat/
featured: false
hidden: false
rating: 4.7

published: false
---

<div class="lang-ko" markdown="1">
# 엣지 포즈 추정을 위한 양자화 인지 훈련 (Quantization-Aware Training, QAT)

스마트 TV, 모바일 칩셋, IoT 게이트웨이와 같은 소비자용 엣지 디바이스에 딥러닝 모델을 배포하기 위해서는 기존의 32비트 부동소수점(FP32) 가중치를 8비트 정수(INT8)로 변환해야 합니다. 훈련 후 양자화(Post-Training Quantization, PTQ)는 간단하게 적용할 수 있지만, **2D/3D 인체 포즈 추정**과 같은 회귀(Regression) 기반 태스크에서는 심각한 정확도 하락을 초래하는 경우가 많습니다.

본 포스트에서는 저전력 엣지 NPU 상에서 정확도를 유지할 수 있도록, 훈련 과정 중에 양자화 노이즈를 명시적으로 모델링하는 **양자화 인지 훈련(Quantization-Aware Training, QAT)** 기법에 대해 설명합니다.

---

## 1. 훈련 후 양자화(PTQ)가 포즈 추정에서 실패하는 이유

HRNet이나 트랜스포머 기반의 키포인트 회귀 모델과 같은 포즈 추정 네트워크는 미세한 좌표 값 변동에 매우 민감합니다.

PTQ는 학습이 완료된 후 검증 데이터를 바탕으로 스케일(Scale)과 제로포인트(Zero-point) 변수를 계산합니다. 이로 인해 다음과 같은 현상이 발생합니다:
* **이상치 클리핑(Outlier clipping):** 활성화 값이 큰 키포인트 어텐션 맵 정보가 잘려나가면서 관절 예측이 심하게 떨리게(jittering) 됩니다.
* **누적 반올림 오차(Accumulated rounding errors):** 깊은 레이어를 거치며 미세한 정밀도 손실이 누적되어 결과적으로 키포인트 검출 위치가 수 픽셀 이상 벗어나게 됩니다.

---

## 2. 훈련 중 양자화 노이즈 모델링

QAT는 훈련 시 순방향 패스(Forward Pass) 과정에 **의사 양자화 노드(Fake-quantization nodes)**를 연산 그래프에 삽입함으로써 이 문제를 해결합니다.

```
[FP32 가중치] ---> [의사 양자화 (Float-INT8-Float)] ---> [양자화된 순방향 패스]
                                                                    |
[FP32 그래디언트] <--- [Straight-Through Estimator (STE)] <----------/
```

* **순방향 패스 (Forward Pass):** 가중치와 활성화 함수 값을 INT8로 양자화한 다음 다시 FP32로 복원(De-quantize)하여 가상으로 정밀도 반올림 오차를 발생시킵니다.
* **역방향 패스 (Backward Pass):** 양자화 단계 함수는 미분이 불가능하므로(거의 모든 구간에서 도함수가 0), **STE(Straight-Through Estimator)**를 사용하여 그래디언트가 의사 양자화 노드를 그대로 통과하도록 우회시킵니다.

이를 통해 모델 파라미터가 훈련 과정 중에 저정밀도 환경에 맞게 적응하므로 배포 시의 정확도 손실을 최소화할 수 있습니다.

---

## 3. ONNX 및 Qualcomm SDK를 활용한 디바이스 배포

최적화된 모델을 배포하는 단계는 다음과 같습니다:
1. QAT 노드가 적용된 PyTorch 모델을 **ONNX** 형식으로 내보냅니다 (QuantizeLinear/DequantizeLinear 연산자를 지원하는 ONNX opset 13 이상 필요).
2. Qualcomm Neural Processing SDK 또는 TensorRT 변환기와 같은 배포 도구를 사용하여 ONNX 양자화 연산자를 타겟 칩셋의 하드웨어 전용 INT8 명령어로 변환합니다.

이러한 QAT 방식을 적용하여 LG 스마트 TV의 저전력 프로세서 상에 실시간 손 포즈 추정 모델을 성공적으로 배포했으며, **3배의 지연 시간 단축(3x latency reduction)**과 함께 **FP32 키포인트 정확도 대비 99% 이상** 수준을 유지할 수 있었습니다.
</div>

<div class="lang-en" markdown="1">
# Quantization-Aware Training (QAT) for Edge Pose Estimation

Deploying deep learning models to consumer edge devices (such as smart TVs, mobile chipsets, and IoT gateways) requires converting 32-bit floating-point (FP32) weights to 8-bit integers (INT8). While Post-Training Quantization (PTQ) is straightforward, it often leads to unacceptable accuracy drops in regression tasks like **2D/3D human pose estimation**.

In this post, we discuss how **Quantization-Aware Training (QAT)** models the quantization noise during training, preserving precision on low-power edge NPUs.

---

## 1. Why Post-Training Quantization Fails on Pose Estimation

Pose estimation networks (such as HRNet or transformer-based keypoint regression models) are highly sensitive to small coordinate shifts. 

PTQ simply calculates scale and zero-point parameters using calibration data after training. This causes:
* **Outlier clipping:** Highly active keypoint attention maps get clipped, leading to jittery joint predictions.
* **Accumulated rounding errors:** Small precision losses compile across deep layers, degrading keypoint localization by several pixels.

---

## 2. Modeling Quantization Noise during Training

QAT solves this by inserting **fake-quantization nodes** into the computation graph during the training forward pass. 

```
[FP32 Weights] ---> [Fake Quantization (Float-INT8-Float)] ---> [Quantized Forward Pass]
                                                                     |
[FP32 Gradients] <--- [Straight-Through Estimator (STE)] <-----------/
```

* **Forward Pass:** The weights and activations are quantized to INT8 and then scaled back to FP32, introducing simulated rounding errors.
* **Backward Pass:** Since the quantization step function is non-differentiable (derivative is zero almost everywhere), we use the **Straight-Through Estimator (STE)** to pass the gradients directly through the fake-quantization nodes unchanged.

This forces the model parameters to adapt to the lower precision limits, minimizing accuracy loss.

---

## 3. Deployment via ONNX and Qualcomm SDK

To deploy the optimized model:
1. Export the PyTorch model with QAT nodes to **ONNX** (utilizing ONNX operator set 13+ which natively supports QuantizeLinear/DequantizeLinear ops).
2. Use converter tools (like Qualcomm Neural Processing SDK or TensorRT converter) to map ONNX quantization operators directly to native INT8 hardware instructions on the target chip.

With QAT, we successfully deployed a real-time hand pose estimation model to LG TVs, achieving **3x latency reduction** while maintaining over **99% of the FP32 keypoint accuracy**.
</div>
