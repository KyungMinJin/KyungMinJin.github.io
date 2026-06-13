---
layout: post
title: "Infant Behavior Video Analysis using Pose Estimation and Action Recognition"
title_ko: "Pose Estimation 및 Action Recognition 기반 영유아 행동 분석 모델 및 활용 제안"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [Pose-Estimation, Action-Recognition, Deep-Learning, Infant-Development]
image: assets/images/infant_pose/page_1.png
description: "A proposal for analyzing infant motor development levels using Deep Dual Consecutive Network (DCPose) and Inflated 3D ConvNet (I3D)."
description_ko: "영유아의 대근육 운동 발달 수준을 평가하고 예측하기 위해 DCPose 및 I3D 모델을 활용한 비디오 행동 분석 솔루션을 제안합니다."
permalink: /posts/infant-behavior-analysis/
featured: false
hidden: false
rating: 4.8
---

<div class="lang-ko" markdown="1">
# Pose Estimation 및 Action Recognition 기반 영유아 행동 분석 모델 및 활용 제안

아동의 성장 과정에서 대근육 발달은 신경 발달 상태를 보여주는 핵심적인 지표입니다. 기존의 발달 검사(예: 베일리, 웩슬러 영유아 발달검사)는 고비용이며 임상 전문가가 대면으로 관찰해야 하므로 시간과 공간의 제약이 큽니다.

본 프로젝트에서는 컴퓨터 비전의 핵심 기술인 **Pose Estimation(자세 추정)** 및 **Action Recognition(행동 인식)** 모델을 결합하여, 집에서 간단히 촬영한 행동 영상만으로 영유아의 발달 상태를 정밀하게 평가하고 예측하는 인공지능 기반 분석 모델 파이프라인을 제안합니다.

---

## 1. 프로젝트 요약 슬라이드

아래 슬라이드는 대학원 재학 중 수행한 영유아 행동 영상 데이터 활용 아이디어 설명서의 세부 장표들입니다.

![1. Cover](/assets/images/infant_pose/page_1.png)

![2. Team Information](/assets/images/infant_pose/page_2.png)

---

## 2. 목표 설정 및 데이터 분석

우리의 주 목표는 두 가지입니다:
1. **정확한 Pose Estimation**을 통한 아동의 관절 움직임 정밀 분석
2. **Action Recognition** 기술을 통한 아동의 대근육 운동 발달 수준(또래 수준, 빠른 수준 등) 예측

![4. Data & Goal](/assets/images/infant_pose/page_4.png)

* **데이터셋 구성**: 다양한 월령대의 아이들 17명을 대상으로, 4가지 촬영 각도에서 측정된 4가지 주요 대근육 행동(공 세우기, 줄 넘기 등) 동영상. 각 프레임별 관절(Joint) 어노테이션 정보 및 발달 단계 메타데이터 포함.

---

## 3. 2D Pose Estimation: DC Pose

영유아의 불규칙하고 빠른 움직임을 추정할 때 발생하는 떨림(Jittering) 현상을 해결하기 위해, 프레임 간 시공간 정보를 통합하는 **DC Pose(Deep Dual Consecutive Network)**를 적용했습니다.

![5. DC Pose Architecture](/assets/images/infant_pose/page_5.png)

* **백본**: COCO Dataset으로 사전 학습된 **HRNet**을 기본 구조로 채택하여 고해상도 특징 맵 유지.
* **시공간 모듈**: 
  * **Pose Residual Fusion**: 연속된 프레임 간의 잔차를 학습하여 가려짐(Occlusion)이나 모션 블러 구간 보정.
  * **Pose Temporal Merger**: 프레임 흐름 간의 시간적 정보를 압축 결합.
  * **Pose Correction Network**: 오추정된 키포인트를 최종 보정.
* **실험 결과**: 관절 히트맵 예측 결과 **99.4%의 Train Accuracy**를 달성하며 매우 정밀한 뼈대 복원에 성공했습니다.

![6. Pose Estimation Result](/assets/images/infant_pose/page_6.png)

---

## 4. Action Recognition: I3D

영상이 주어졌을 때 영유아가 어떠한 발달 수준의 행동을 보이는지 판별하기 위해 3차원 합성곱 신경망인 **I3D (Inflated 3D Convolutional Network)**를 활용했습니다.

![7. I3D Model](/assets/images/infant_pose/page_7.png)

* **핵심 원리**: 잘 훈련된 2D CNN(ImageNet으로 학습된 Inception-V1)의 가중치를 시간 축으로 팽창(Inflating)시켜 3D 필터($N \times N \times N$)로 확장 적용.
* **장점**: 기존의 2D CNN + LSTM 구조에 비해 시공간적(Spatio-temporal) 특징을 직접 표현할 수 있어 비디오 행동 인식 분야에서 성능이 탁월함.
* **실험 결과**: 총 231개의 발달 행동 검증용 영상 중 229개를 맞추며 **98%의 최종 분류 정확도(Total Accuracy 0.98)**를 얻었습니다.

![8. Action Recognition Result](/assets/images/infant_pose/page_8.png)

---

## 5. 결론 및 실무 활용방안

이 기술은 원격 영유아 케어 서비스 및 사고 예방 분야로 확장 가능합니다.

![9. Conclusion](/assets/images/infant_pose/page_9.png)

* **자세 분석을 통한 위험 예방**: 영아의 관절 위치 변화 속도를 실시간 추정하여 낙상, 뒤집기 질식 등의 위험 상황을 탐지하거나 사고 원인을 사전에 규명할 수 있습니다.
* **비대면 아동 발달 스크리닝**: 병원을 방문하기 힘든 가정에서도 모바일 앱 등으로 촬영한 영유아의 일상 운동 놀이 영상을 통해 베일리 발달검사 등을 대체할 수 있는 신뢰성 높은 1차 발달 평가 리포트를 받아볼 수 있습니다.
</div>

<div class="lang-en" markdown="1">
# Infant Behavior Video Analysis using Pose Estimation and Action Recognition

Gross motor skill development in early childhood serves as a critical biomarker for neurodevelopmental health. Conventional evaluation tools, such as the Bayley Scales of Infant Development, are expensive and require in-person observation by clinical experts, which limits accessibility.

This project proposes an artificial intelligence pipeline that combines **Pose Estimation** and **Action Recognition** to precisely evaluate and predict infant motor development using everyday videos recorded at home.

---

## 1. Project Summary Slides

The slides below present the detailed proposal for using infant behavior video datasets, developed during my graduate studies.

![1. Cover](/assets/images/infant_pose/page_1.png)

![2. Team Information](/assets/images/infant_pose/page_2.png)

---

## 2. Goals & Data Analysis

We set two main objectives:
1. Joint-level precision tracking using **Pose Estimation**
2. Predicting developmental stages (e.g., advanced vs. typical age levels) using **Action Recognition**

![4. Data & Goal](/assets/images/infant_pose/page_4.png)

* **Dataset**: Video records of 17 infants at different developmental stages, recorded from 4 camera angles during 4 gross motor tasks (e.g., stopping a rolling ball, jumping rope). Ground truth joint annotations and developmental stage metadata are included.

---

## 3. 2D Pose Estimation: DC Pose

To prevent joint jittering caused by infants' rapid, irregular movements, we adopted **DC Pose (Deep Dual Consecutive Network)**, which integrates spatial-temporal information across consecutive frames.

![5. DC Pose Architecture](/assets/images/infant_pose/page_5.png)

* **Backbone**: Uses a **HRNet** pre-trained on the COCO Dataset to maintain high-resolution feature maps.
* **Spatiotemporal Modules**: 
  * **Pose Residual Fusion**: Learns motion residuals to correct occlusion and motion blur.
  * **Pose Temporal Merger**: Aggregates temporal cues across consecutive frames.
  * **Pose Correction Network**: Refines misaligned joint predictions.
* **Results**: Achieved a **Train Accuracy of 99.4%**, demonstrating highly precise keypoint regression.

![6. Pose Estimation Result](/assets/images/infant_pose/page_6.png)

---

## 4. Action Recognition: I3D

To categorize the motor coordination level of the infant's movements, we utilized the **I3D (Inflated 3D Convolutional Network)**.

![7. I3D Model](/assets/images/infant_pose/page_7.png)

* **Core Principle**: Extends pre-trained 2D Inception-V1 filters into 3D filters ($N \times N \times N$) along the temporal dimension.
* **Advantages**: Captures spatiotemporal features directly, outperforming hybrid 2D CNN + LSTM architectures in video recognition tasks.
* **Results**: Successfully predicted developmental categories for 229 out of 231 validation clips, achieving a **Total Accuracy of 0.98**.

![8. Action Recognition Result](/assets/images/infant_pose/page_8.png)

---

## 5. Conclusion & Potential Applications

This technology can be applied to remote child care services and home safety systems.

![9. Conclusion](/assets/images/infant_pose/page_9.png)

* **Accident Prevention**: Real-time velocity tracking of infant joints can help detect dangerous events (e.g., rollover suffocation, falls) or analyze the causes of accidents.
* **Non-contact Screening**: Allows parents to upload videos of home play tasks to receive highly reliable preliminary screening reports, reducing the cost and accessibility barriers of traditional face-to-face clinic visits.
</div>
