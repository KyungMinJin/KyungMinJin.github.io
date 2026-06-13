---
layout: post
title: "From HANet to M-HANet: Kinematic Continuity-Aware Attention for Video Pose Estimation"
title_ko: "HANet에서 M-HANet까지: 비디오 포즈 추정을 위한 물리 법칙 기반 어텐션 구조 분석"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [Pose-Estimation, Transformer, Kinematics, WACV-2023, Journal-Neural-Networks]
image: assets/images/publications/action_aware_wacv2023_page1.png
description: "A comprehensive review of HANet (WACV 2023 Oral) and M-HANet (Neural Networks 2024), focusing on how to model physical laws like velocity and acceleration in spatial-temporal transformers."
description_ko: "인체 관절의 물리적 운동 법칙(속도/가속도)을 트랜스포머의 어텐션 맵에 직접 인코딩하여 비디오 포즈 떨림을 제어하는 HANet(WACV 2023 Oral) 및 Masked-HANet(Neural Networks 2024) 프레임워크를 분석합니다."
permalink: /posts/hanet-to-mhanet-kinematics/
featured: false
hidden: false
rating: 4.9
---

<div class="lang-ko" markdown="1">
# HANet에서 M-HANet까지: 비디오 포즈 추정을 위한 물리 법칙 기반 어텐션 구조 분석

비디오 기반 2D/3D 인체 포즈 추정(Human Pose Estimation)에서 단일 이미지 모델(Frame-by-frame detector)을 그대로 사용하면 가장 흔하게 마주하는 문제는 **프레임 간 예측값의 미세한 흔들림(Jittering/Trembling)**입니다. 

인간은 물리적으로 순간 이동을 하거나 관절이 비이상적인 속도로 꺾이지 않습니다. 즉, 인체의 관절 움직임은 일정한 **물리적 속도와 가속도의 연속성(Kinematic Continuity)**을 가집니다. 

본 포스트에서는 이러한 물리적 제약 조건을 트랜스포머의 어텐션 메커니즘에 직접 주입하여 학습 시 흔들림을 원천 억제하는 **HANet (WACV 2023 Oral)**과, 이를 자가지도 마스킹 기법으로 고도화하여 국제 학술지 *Neural Networks (2024)*에 게재된 **M-HANet (Masked-HANet)**의 설계 개념을 분석합니다.

---

## 1. HANet (WACV 2023 Oral): 운동 기하학적 정보의 어텐션 주입

기존의 시공간 트랜스포머(Spatial-Temporal Transformer)들은 시간 축 방향으로 어텐션 연산을 수행하여 프레임 간 유사한 영역을 쫓아다니게 만들었습니다. 하지만 이는 단순히 시각적 특징(Visual Features)의 매칭에 의존하므로, 모션 블러가 생기거나 조도가 급변하면 오추정을 범하게 됩니다.

HANet은 **"관절의 시간적 궤적은 뉴턴의 물리 운동 법칙을 따른다"**는 직관에서 출발했습니다.

![HANet Concept](/assets/images/HANet.png)

### ① Kinematic Representation
임의의 관절 $J$의 $t$ 프레임에서의 위치를 $P_t$라 할 때, 속도 $V_t$와 가속도 $A_t$를 피처 레벨에서 정량화하여 토큰으로 정의합니다:
* **속도 토큰 (Velocity Token)**: $V_t = P_t - P_{t-1}$
* **가속도 토큰 (Acceleration Token)**: $A_t = V_t - V_{t-1} = P_t - 2P_{t-1} + P_{t-2}$

### ② Hierarchical Attention Module
추출된 기하학적 토큰($P, V, A$)들은 아래 계층 구조를 거쳐 학습됩니다:
* **Spatial Attention**: 단일 프레임 내 관절 구조적 링크 학습.
* **Temporal Kinematic Attention**: 각 관절의 $V_t$와 $A_t$ 토큰을 시간 방향의 Query/Key/Value 연산에 더해주어(Residual Connection), 속도 벡터와 가속도 벡터의 진행 방향이 물리적으로 일관되도록 어텐션 가중치 유도.

이를 통해 후처리 필터(Kalman, Savitzky-Golay 등) 없이도 모델 출력 단에서 직접 **물리적으로 부드러운(Smooth) 관절 궤적**이 복원되는 놀라운 결과를 도출했습니다.

---

## 2. M-HANet (Neural Networks 2024): 마스킹과 자가 지도 기법의 융합

저널 버전으로 확장된 **M-HANet (Masked-HANet)**은 "물리 법칙을 더 가혹한 환경에서도 잘 학습하게 할 방법이 없을까?"라는 고민에서 탄생했습니다.

### ① Masked Kinematic Continuity 학습
* **핵심 메커니즘**: 입력 비디오 토큰 중 특정 프레임 구간의 속도/가속도 정보를 인위적으로 지우거나 노이즈를 섞어 입력합니다.
* **학습 목표**: 모델은 가려지거나 왜곡된 물리 토큰 상태에서도, 이전 프레임들의 속도 진행 방향성과 가속도 벡터를 역산하여 빈 구간의 키포인트 궤적을 **물리 법칙에 부합하도록 원복(Reconstruct)**해내도록 자가지도 마스킹 손실함수(Masked Reconstruction Loss)를 통해 고도화 학습됩니다.
* 이 학습 기법은 현업 임베디드(Smart TV 등) 환경에서 **일부 관절이 완전히 프레임 아웃되어 가려지더라도, 이전 관절 모션을 기반으로 물리 궤적을 완벽히 복원**해내는 뛰어난 내구성을 보장합니다.

---

## 3. 실험 성과 및 의의

* **벤치마크 최고 성능(SOTA) 달성**: 비디오 포즈 추정의 핵심 벤치마크인 **AIST**, **JHMDB**, **3D PW** 데이터셋에서 기존 강자(DcPose, VIBE 등)를 제치고 당시 가장 뛰어난 추정 정확도(MPJPE 및 PCKh@0.5)를 입증했습니다.
* **LG Smart TV 에지 탑재 성공**: 이 연구 성과는 단순 논문에 그치지 않고, 가벼운 파라미터 튜닝을 거쳐 **LG 스마트 TV 에지 디바이스**에 탑재되어 실제 사용자의 홈 트레이닝 및 댄스 가이드 동작 분석 알고리즘의 핵심 엔진으로 상용화 기여했습니다.

물리적인 법칙(Domain Physics)을 인공지능 모델 구조 내에 인코딩(Physics-informed Neural Network)하는 설계적 패러다임이 비디오 이해 기술을 어떻게 비약적으로 개선할 수 있는지 보여준 대표적인 사례입니다.
</div>

<div class="lang-en" markdown="1">
# From HANet to M-HANet: Kinematic Continuity-Aware Attention for Video Pose Estimation

In video-based 2D and 3D Human Pose Estimation (HPE), the most frequent issue encountered when applying a frame-by-frame detector directly is **high-frequency coordinate jittering (trembling)**. 

Physically, human joints do not teleport or bend at impossible speeds. That is, human motion possesses **kinematic continuity** governed by velocity and acceleration constraints. 

In this post, we analyze the architectural designs of **HANet (WACV 2023 Oral)**, which embeds physical properties directly into the spatial-temporal attention mechanism, and its journal extension **M-HANet (Masked-HANet)** published in *Neural Networks (2024)*.

---

## 1. HANet (WACV 2023 Oral): Injecting Physical Constraints into Attention

Standard spatial-temporal transformers compute attention maps over time to match visual features across frames. However, this visual-matching approach fails when encountering motion blur or rapid lighting changes.

HANet was born from the intuition that **the temporal trajectory of human joints must comply with Newton's laws of motion**.

![HANet Concept](/assets/images/HANet.png)

### ① Kinematic Representation
Let $P_t$ represent the coordinate of joint $J$ at frame $t$. We mathematically define velocity ($V_t$) and acceleration ($A_t$) tokens at the feature level:
* **Velocity Token**: $V_t = P_t - P_{t-1}$
* **Acceleration Token**: $A_t = V_t - V_{t-1} = P_t - 2P_{t-1} + P_{t-2}$

### ② Hierarchical Attention Module
These parsed physical tokens ($P, V, A$) are processed hierarchically:
* **Spatial Attention**: Models structural relationships within a single frame.
* **Temporal Kinematic Attention**: Adds the $V_t$ and $A_t$ tokens to the Query/Key/Value queries via residual connections. This forces the temporal attention weights to favor motion trajectories that are physically consistent.

This mechanism enables the model to output **physically smooth joint trajectories** directly, eliminating the need for post-processing filters (such as Kalman or Savitzky-Golay filters).

---

## 2. M-HANet (Neural Networks 2024): Integrating Self-Supervised Masking

**M-HANet (Masked-HANet)**, the extended journal version, leverages self-supervised masking to further enhance physical constraint learning.

### ① Masked Kinematic Continuity Learning
* **Mechanism**: During training, we artificially mask or inject noise into the velocity and acceleration tokens of random frame intervals.
* **Objective**: The model is optimized using a Masked Reconstruction Loss, forcing it to reconstruct the missing keypoint coordinates by extrapolating the trajectory vectors of preceding frames.
* This strategy ensures excellent robustness in real-world deployment (e.g., Smart TVs), where **the model can seamlessly predict joint positions even if a limb temporarily exits the frame**.

---

## 3. Experimental Results & Real-world Impact

* **State-of-the-Art (SOTA) Benchmarks**: Proved top-tier performance on **AIST**, **JHMDB**, and **3D PW** datasets, outperforming established methods like DcPose and VIBE.
* **LG Smart TV Deployment**: The research was optimized for resource-constrained platforms, converted via ONNX, and successfully deployed to **LG Smart TV edge processors** to power interactive home fitness and dance coaching applications.

M-HANet showcases how embedding domain-specific physics into AI model architectures (Physics-informed AI) can fundamentally resolve engineering challenges in video understanding.
</div>
