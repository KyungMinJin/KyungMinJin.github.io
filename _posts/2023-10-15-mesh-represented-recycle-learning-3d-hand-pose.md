---
layout: post
title: "Mesh Represented Recycle Learning for 3D Hand Pose and Mesh Estimation"
title_ko: "3D 손 포즈 및 메쉬 복원을 위한 메쉬 표상 재활용 학습법"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [Hand-Pose, Mesh-Recovery, Self-Supervised-Learning, arXiv-2023]
image: assets/images/publications/mesh_recycle_pipeline.jpg
description: "A summary of our paper introducing a mesh-represented recycle learning framework designed to reconstruct 3D hands without dense human annotations."
description_ko: "3차원 손 메쉬 및 관절 추정의 정확도를 극대화하기 위해, 합성 데이터(Synthetic data)와 실데이터 간의 도메인 갭을 극복하는 메쉬 재활용 학습(Recycle Learning) 기법에 대해 분석합니다."
permalink: /posts/recyclenet-hand-mesh/
featured: false
hidden: false
rating: 4.8
---

<div class="lang-ko" markdown="1">
# 3D 손 포즈 및 메쉬 복원을 위한 메쉬 표상 재활용 학습법

스마트 TV, VR/AR 기기 등 인간-컴퓨터 상호작용(HCI)의 활용이 극대화되면서 사용자의 **3차원 손 포즈 및 핸드 메쉬(3D Hand Mesh)**를 정확하게 복원하는 기술이 중요해졌습니다. 하지만 실제 카메라 영상에서 손가락 관절의 3D 좌표 및 조밀한 3D 메쉬 버텍스(Vertices) 정답을 라벨링하는 것은 장비의 한계상 불가능에 가깝습니다.

이 때문에 그래픽스 툴로 정밀 생성된 **합성 데이터(Synthetic data)**로 학습한 뒤 실세계 데이터에 적용하지만, 배경, 피부 질감, 조명 차이로 발생하는 **도메인 갭(Domain Gap)**으로 인해 실제 TV 카메라 환경에서는 손가락이 구부러지는 궤적을 쫓지 못하는 현상이 생깁니다.

본 포스트에서는 2023년 arXiv에 투고된 **Mesh Represented Recycle Learning (RecycleNet)** 연구의 재배치 파이프라인과 3D 손 복원 아키텍처를 소개합니다.

---

## 1. 도메인 갭(Domain Gap) 극복을 위한 기존 방식의 한계

합성 데이터로 학습된 3D Hand Estimator 모델을 실제 손 이미지에 테스트하면 손가락이 꼬이거나 깊이(Depth)가 뭉개집니다.
* 일반적인 도메인 적응(Domain Adaptation) 기법들은 피처 수준의 정렬에 초점을 맞추어 정밀한 손가락 끝점(Fingertip)의 회귀 성능이 저하되는 한계가 있었습니다.

---

## 2. RecycleNet 핵심 아키텍처: Recycle Learning Loop

RecycleNet은 이미지 피처에 직접 손을 대는 대신, 추정된 **3D 메쉬 결과물 자체를 재활용하여 정제(Refinement)**하는 순환 구조(Recycle Learning Loop)를 취합니다.

![RecycleNet Pipeline](/assets/images/publications/mesh_recycle_pipeline.jpg)

### ① Synthetic-to-Real Recycle Pipeline
* **Step 1**: 합성 데이터로 학습된 초기 예측 모델이 실제 무라벨 손 이미지(Unlabeled Real Image)로부터 3D Hand Mesh 파라미터(MANO 모델 파라미터)를 1차 예측합니다.
* **Step 2**: 1차 예측된 3D 메쉬 표상(Mesh Representation)을 다시 렌더링(Rendering)하여, 실세계 이미지의 실루엣 및 2D 관절 추정값과 매칭하는 자기지도 손실함수(Projection Loss & Silhouette Loss)를 설계합니다.
* **Step 3 (Recycle)**: 실제 도메인의 렌더링된 메쉬를 다시 모델의 입력 데이터셋 풀에 피드백하여, 합성 도메인 가중치와 실제 도메인 피드백 루프가 균형을 이루도록 순환적으로 가중치를 업데이트(Recycle training)합니다.

### ② Finger-grouping Attention Mechanism
* 다섯 손가락 관절 간의 간섭(Interference)을 줄이고 독립적인 미세 동작을 포착하기 위해, 손가락 군별(Thumb, Index, Middle, Ring, Pinky)로 어텐션 가중치 영역을 나누어 연산하는 그룹핑 어텐션(Grouping Attention)을 적용하여 SOTA 성능(PA-MPJPE 향상)을 확보했습니다.

---

## 3. 결론 및 실무 의의

RecycleNet은 3D 메쉬의 기하학적 형상(Geometry) 정보를 학습 알고리즘 내부에서 재순환(Recycle)시킴으로써, 대규모 3D 실세계 정답 데이터 없이도 실세계 이미지 상의 손가락 끝점 복원 정확도를 비약적으로 향상시켰습니다. 본 연구 성과는 **LG 스마트 TV의 손동작 제어 인식 솔루션** 및 가상 스마트 어시스턴트 컨트롤러의 포즈 엔진 고도화에 직접적으로 기여했습니다.
</div>

<div class="lang-en" markdown="1">
# Mesh Represented Recycle Learning for 3D Hand Pose and Mesh Estimation

Reconstructing **3D Hand Poses and Meshes** is critical for next-generation Human-Computer Interaction (HCI) in VR, AR, and smart TVs. However, annotating 3D joint coordinates and dense mesh vertices in real-world images is practically impossible.

Although models trained on **synthetic data** offer a starting point, they fail under the **domain gap** (differences in background, lighting, and texture), causing hand movements to jitter in real TV cameras.

This post highlights **Mesh Represented Recycle Learning (RecycleNet)**, published on arXiv in 2023.

---

## 1. Domain Adaptations Limitations

Applying synthetic-trained estimators to real-world hand images often results in distorted fingers or depth compression.
* Standard domain adaptation methods align high-level features but fail to preserve local joint structures, leading to inaccurate fingertip tracking.

---

## 2. Core Concepts: Recycle Learning Loop

Instead of aligning intermediate feature maps, RecycleNet recycles the predicted **3D mesh outputs** to self-supervise the network.

![RecycleNet Pipeline](/assets/images/publications/mesh_recycle_pipeline.jpg)

### ① Synthetic-to-Real Recycle Pipeline
* **Step 1**: The initial network trained on synthetic data estimates 3D hand mesh parameters (using the MANO model) from unlabeled real images.
* **Step 2**: The estimated 3D mesh is re-projected back onto the 2D plane to compute self-supervised silhouette and 2D joint alignment losses.
* **Step 3 (Recycle)**: The real-domain rendered mesh outputs are recycled back into the training pool, enabling a cyclic optimization process that balances synthetic features with real-world geometries.

### ② Finger-grouping Attention Mechanism
* To minimize keypoint cross-interference, we group attention maps by finger (Thumb, Index, Middle, Ring, Pinky), enabling high-fidelity fingertip tracking.

---

## 3. Industrial Impact

By recycling 3D mesh representations, RecycleNet improves 3D hand tracking on real-world inputs without dense hand annotations. This methodology served as a core engine for **LG Smart TV hand-gesture control systems** and smart assistant controllers.
</div>
