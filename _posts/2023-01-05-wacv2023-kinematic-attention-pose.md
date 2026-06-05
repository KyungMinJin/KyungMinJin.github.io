---
layout: post
title: "[WACV 2023 Oral] Kinematic-aware Hierarchical Attention Network for Video Pose Estimation"
title_ko: "[WACV 2023 Oral] 비디오 포즈 추정을 위한 운동학 인지 계층적 어텐션 네트워크"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [WACV, Pose-Estimation, Attention, Deep-Learning]
image: assets/images/HANet.png
description: "A summary of our WACV 2023 Oral paper introducing a kinematic continuity-aware hierarchical attention network for video-based human pose estimation."
description_ko: "비디오 기반 인체 포즈 추정을 위해 물리적 관절 구조 및 운동 법칙(속도, 가속도)을 활용하는 계층적 어텐션 네트워크를 제안한 WACV 2023 구두 발표 논문 요약입니다."
permalink: /posts/hanet/
featured: true
hidden: false
rating: 5.0
---

<div class="lang-ko" markdown="1">
# [WACV 2023 Oral] 비디오 포즈 추정을 위한 운동학 인지 계층적 어텐션 네트워크

비디오 기반 3차원 인체 포즈 추정에서, 프레임 간 **시간적 및 운동학적 일관성(temporal and kinematic consistency)**을 유지하는 것은 매우 까다로운 과제입니다. 기존의 프레임별 포즈 추정기들은 물리적인 골격 관절 구조나 해부학적 한계를 명시적으로 모델링하지 않기 때문에, 예측값의 미세한 흔들림(jittering), 관절 뒤바뀜 오류(joint swap errors), 급격한 움직임이나 가려짐(occlusion) 상태에서의 추정 실패 등을 빈번히 겪게 됩니다.

본 논문(WACV 2023 구두 발표 선정작)에서는 물리적 운동 법칙을 바탕으로 관절 간의 관계와 시간적 연속성을 인코딩하여 이러한 한계를 극복하는 **운동학 인지 계층적 어텐션 네트워크(Kinematic-aware Hierarchical Attention Network, KHAN / HANet)**를 제안합니다.

---

## 1. 모델 아키텍처 (HANet)

다음은 운동학 인지 계층적 어텐션 네트워크의 전체 아키텍처입니다. 입력 프레임들로부터 공간적 키포인트 특징을 추출한 뒤, 인체 골격 구조를 따라 시간적 문맥을 전파합니다.

<div class="text-center my-4">
    <img src="{{ site.baseurl }}/assets/images/HANet.png" class="img-fluid rounded shadow-lg border" alt="HANet 모델 아키텍처" style="max-height: 500px; width: 100%; object-fit: contain;">
    <p class="text-muted mt-2" style="font-size: 0.85rem;">그림 1: 계층적 어텐션 블록과 시공간 인코더를 포함하는 HANet의 전체 파이프라인.</p>
</div>

네트워크는 다음과 같은 두 가지 핵심 요소로 구성됩니다:
1. **계층적 어텐션 인코더 (Hierarchical Attention Encoder):** 서로 다른 해상도 레이어로부터 멀티스케일 시공간 어텐션을 계산합니다.
2. **운동학 인지 특징 파이프라인 (Kinematic-aware Feature Pipeline):** 키포인트 예측을 유도하기 위해 속도(velocity)와 가속도(acceleration)를 명시적으로 모델링합니다.

---

## 2. 운동학적 특징 기반 동적 시공간 어텐션

트랜스포머 모델의 표준 셀프 어텐션 매커니즘은 인체 골격 구조를 고려하지 않고 모든 키포인트를 동등하게 취급합니다. 반면, HANet은 **운동학적 관절 구조(kinematic joints)**에 따라 어텐션을 계층적으로 세분화하여 연산합니다.

* **국소 어텐션 (Local Attention):** 뼈대(bone)로 직접 연결된 인접 관절 사이(예: 손목과 팔꿈치, 팔꿈치와 어깨)에서 어텐션을 계산합니다.
* **전역 어텐션 (Global Attention):** 양손의 협동 동작과 같이 거리가 먼 관절 간의 장기 의존성(long-range dependencies)을 포착합니다.

### 운동학적 특징 공식화 (Kinematic Feature Formulation)
물리적 운동 법칙을 신경망에 주입하기 위해, 시계열 좌표 정보를 바탕으로 키포인트의 동적 운동 특징을 계산합니다. $t$ 프레임에서 특정 관절의 $d$차원 좌표(2D 또는 3D)를 $p_t \in \mathbb{R}^d$라 정의할 때, 다음과 같이 속도와 가속도를 유도합니다:

* **속도 ($v_t$):**
  $$v_t = p_t - p_{t-1}$$

* **가속도 ($a_t$):**
  $$a_t = v_t - v_{t-1} = p_t - 2p_{t-1} + p_{t-2}$$

이러한 운동학적 특징들은 최초의 관절 임베딩과 결합(concatenation)되어, 급격한 움직임이나 심한 가려짐 상황에서도 물리적인 궤적을 외삽(extrapolate)함으로써 부드럽고 안정적인 추정을 가능하게 만듭니다.

### 계층적 어텐션 스케일링
쿼리 $Q$, 키 $K$, 밸류 $V$가 주어졌을 때, 어텐션 맵은 아래 공식으로 계산됩니다:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

희소한(sparse) 지도 신호 하에서 학습이 불안정해지는 것을 방지하기 위해, 계층적 인코더는 모든 레이어 $l \in \{1, \dots, L\}$의 멀티스케일 특징 맵을 결합합니다:
$$F_{\text{agg}} = \sum_{l=1}^L w_l \cdot F^{(l)}$$
여기서 $F^{(l)}$는 레이어 $l$에서의 어텐션 특징을 의미하며, $w_l$은 학습 가능한 스케일링 가중치입니다.

---

## 3. 시각적 데모 (HANet 실제 구동 예시)

다음은 JHMDB, AIST++, 3DPW 데이터셋에서 평가된 HANet의 정성적 추정 결과로, 일관되고 매끄러운 3차원 인체 관절 및 SMPL 메쉬 복원 성능을 확인할 수 있습니다.

### A. 2D 포즈 트래킹 (JHMDB 데이터셋)
빠른 스윙 동작과 강한 모션 블러가 있는 상황에서도 키포인트가 안정적으로 유지되는 것을 확인할 수 있습니다.

<div class="text-center my-4">
    <img src="{{ site.baseurl }}/assets/images/jhmdb.gif" class="img-fluid rounded shadow-sm border" alt="JHMDB 데이터셋에서의 HANet 2D 포즈 트래킹" style="max-height: 350px;">
    <p class="text-muted mt-2" style="font-size: 0.85rem;">데모 1: 역동적인 움직임 상황에서의 2D 골격 추정 (Sub-JHMDB).</p>
</div>

---

### B. 3D 포즈 추정 및 SMPL 메쉬 복원 (AIST++ 데이터셋)
복잡한 댄스 동작 상황에서 3차원 관절 및 부드러운 SMPL 인체 메쉬 표면을 복원해 냅니다.

<div class="row text-center my-4">
    <div class="col-md-6 mb-3">
        <img src="{{ site.baseurl }}/assets/images/aist_3D.gif" class="img-fluid rounded shadow-sm border" alt="AIST++ 데이터셋에서의 HANet 3D 관절 추정" style="max-height: 250px; width: 100%; object-fit: cover;">
        <p class="text-muted mt-2" style="font-size: 0.85rem;">HANet: 3차원 관절 좌표 출력값.</p>
    </div>
    <div class="col-md-6 mb-3">
        <img src="{{ site.baseurl }}/assets/images/aist_smpl.gif" class="img-fluid rounded shadow-sm border" alt="AIST++ 데이터셋에서의 HANet SMPL 메쉬 복원" style="max-height: 250px; width: 100%; object-fit: cover;">
        <p class="text-muted mt-2" style="font-size: 0.85rem;">HANet: 복원된 SMPL 인체 메쉬.</p>
    </div>
</div>

---

### C. 야외 환경에서의 3D 바디 메쉬 복원 (3DPW 데이터셋)
도전적인 야외 환경 데이터셋인 3DPW 상의 평가 결과로, 가려짐과 빠른 동작 속에서도 강건한 포즈 복원 및 바디 형태 피팅을 보여줍니다.

<div class="text-center my-4">
    <img src="{{ site.baseurl }}/assets/images/pw3d_smpl.gif" class="img-fluid rounded shadow-sm border" alt="3DPW 데이터셋에서의 HANet 3D 메쉬 복원" style="max-height: 350px;">
    <p class="text-muted mt-2" style="font-size: 0.85rem;">데모 2: 야외 가려짐 및 빠른 움직임 환경에서의 부드러운 3D 인체 메쉬 복원.</p>
</div>

---

## 4. 온라인 상호 지도학습 (Online Cross-Supervision) 및 성능 지표

최초 입력 좌표 정보와 최종 정제된 출력값 간의 결합 최적화를 위해 **온라인 상호 학습(online mutual learning)** 목적 함수를 사용합니다. 학습 손실값에 따라 네트워크는 동적으로 지도 대상을 선택합니다:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{pose}} + \lambda_{\text{mutual}} \mathcal{L}_{\text{mutual}}(\pi_{\theta_{\text{in}}}, \pi_{\theta_{\text{out}}})$$

### 정량적 성능 비교

제안하는 방법론은 주요 벤치마크 데이터셋에서 최고 성능(SOTA)을 달성했습니다:

| 데이터셋 | 평가 지표 | 입력 베이스라인 | **HANet (본 연구)** | 성능 향상폭 |
|:---|:---|:---:|:---:|:---:|
| **Sub-JHMDB (2D)** | PCK @ 0.05 | 57.3% | **91.9%** | **+34.6%** |
| **Human3.6M (3D)** | MPJPE (mm) | 54.6mm | **52.8mm** | **-1.8mm** |
| **AIST++ (3D)** | MPJPE (mm) | 107.7mm | **69.2mm** | **-38.5mm** |
| **3DPW (SMPL)** | MPJPE (mm) | 78.9mm | **77.1mm** | **-1.8mm** |

---

### 주요 링크 및 자료
* **논문:** [CVF Open Access Paper](https://openaccess.thecvf.com/content/WACV2023/html/Jin_Kinematic-Aware_Hierarchical_Attention_Network_for_Human_Pose_Estimation_in_WACV_2023_paper.html)
* **코드:** [GitHub Repository (KyungMinJin/HANet)](https://github.com/KyungMinJin/HANet)
</div>

<div class="lang-en" markdown="1">
# [WACV 2023 Oral] Kinematic-aware Hierarchical Attention Network for Video Pose Estimation

In video-based human pose estimation, maintaining **temporal and kinematic consistency** across frames is a major challenge. Standard frame-by-frame pose estimators often suffer from jittery predictions, joint swap errors, and failure under fast motion or occlusion because they do not model physical skeletal joints and anatomical limits.

Our paper, presented as an **Oral presentation at WACV 2023**, proposes the **Kinematic-aware Hierarchical Attention Network (KHAN / HANet)** to resolve these issues by explicitly encoding joint relations and temporal continuity based on physical laws of motion.

---

## 1. Model Architecture (HANet)

Below is the overall architecture of the Kinematic-aware Hierarchical Attention Network. It extracts spatial keypoint features and propagates temporal context across skeletal structures.

<div class="text-center my-4">
    <img src="{{ site.baseurl }}/assets/images/HANet.png" class="img-fluid rounded shadow-lg border" alt="HANet Model Architecture" style="max-height: 500px; width: 100%; object-fit: contain;">
    <p class="text-muted mt-2" style="font-size: 0.85rem;">Figure 1: Overall pipeline of HANet showcasing Hierarchical Attention blocks and Spatio-Temporal encoders.</p>
</div>

The network incorporates two main components:
1. A **Hierarchical Attention Encoder** that computes multi-scale spatio-temporal attention from different resolution layers.
2. A **Kinematic-aware Feature Pipeline** that explicitly models velocity and acceleration to guide keypoint predictions.

---

## 2. Dynamic Spatial & Temporal Attention with Kinematic Features

Standard self-attention mechanisms in transformers treat all keypoints in a human body equally, ignoring the physical structure of the skeleton. In contrast, HANet structures attention hierarchically based on **kinematic joints**:

* **Local Attention:** Computes attention within adjacent joints (e.g., connecting wrist to elbow, elbow to shoulder) representing physical bone links.
* **Global Attention:** Captures long-range dependencies (e.g., left hand to right hand coordinating during an action).

### Kinematic Feature Formulation
To enforce the physical laws of motion, we compute keypoint motion features based on sequential coordinates. Let $p_t \in \mathbb{R}^d$ be the $d$-dimensional coordinate (2D or 3D) of a body joint at frame $t$. We define the kinematic features as follows:

* **Velocity ($v_t$):**
  $$v_t = p_t - p_{t-1}$$

* **Acceleration ($a_t$):**
  $$a_t = v_t - v_{t-1} = p_t - 2p_{t-1} + p_{t-2}$$

These features are concatenated with the initial joint embeddings, enabling the network to learn smooth trajectories and handle heavy occlusion by extrapolating physical motion paths.

### Hierarchical Attention Scaling
Given query $Q$, key $K$, and value $V$, the attention map is calculated as:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

To prevent training instability under sparse supervision, our hierarchical encoder aggregates multi-scale feature maps from all layers $l \in \{1, \dots, L\}$:
$$F_{\text{agg}} = \sum_{l=1}^L w_l \cdot F^{(l)}$$
where $F^{(l)}$ represents the attention features at layer $l$, and $w_l$ is a learnable scaling weight.

---

## 3. Visual Demonstrations (HANet in Action)

Below are the qualitative tracking results of HANet evaluated on JHMDB, AIST++, and 3DPW datasets, demonstrating its ability to reconstruct poses and 3D SMPL meshes with smooth continuity.

### A. 2D Pose Tracking (JHMDB Dataset)
Notice the stable keypoint tracking even during fast swinging motions and heavy motion blur.

<div class="text-center my-4">
    <img src="{{ site.baseurl }}/assets/images/jhmdb.gif" class="img-fluid rounded shadow-sm border" alt="HANet 2D tracking on JHMDB" style="max-height: 350px;">
    <p class="text-muted mt-2" style="font-size: 0.85rem;">Demo 1: 2D skeletal estimation under fast motion dynamics (Sub-JHMDB).</p>
</div>

---

### B. 3D Pose Estimation & SMPL Mesh Recovery (AIST++ Dataset)
Reconstruction of 3D skeletal joints and smooth SMPL body mesh surfaces under complex dance movements.

<div class="row text-center my-4">
    <div class="col-md-6 mb-3">
        <img src="{{ site.baseurl }}/assets/images/aist_3D.gif" class="img-fluid rounded shadow-sm border" alt="HANet 3D joints on AIST" style="max-height: 250px; width: 100%; object-fit: cover;">
        <p class="text-muted mt-2" style="font-size: 0.85rem;">HANet: 3D joint coordinate outputs.</p>
    </div>
    <div class="col-md-6 mb-3">
        <img src="{{ site.baseurl }}/assets/images/aist_smpl.gif" class="img-fluid rounded shadow-sm border" alt="HANet SMPL mesh on AIST" style="max-height: 250px; width: 100%; object-fit: cover;">
        <p class="text-muted mt-2" style="font-size: 0.85rem;">HANet: Reconstructed SMPL body mesh.</p>
    </div>
</div>

---

### C. 3D Body Mesh Recovery (3DPW Dataset)
Evaluation on the challenging in-the-wild 3DPW dataset, demonstrating robust pose restoration and shape fitting.

<div class="text-center my-4">
    <img src="{{ site.baseurl }}/assets/images/pw3d_smpl.gif" class="img-fluid rounded shadow-sm border" alt="HANet 3D body mesh on 3DPW" style="max-height: 350px;">
    <p class="text-muted mt-2" style="font-size: 0.85rem;">Demo 2: Smooth 3D body mesh recovery under physical occlusions and fast motion in the wild.</p>
</div>

---

## 4. Online Cross-Supervision & Results

To enable joint optimization between the initial input coordinates and the final refined outputs, we utilize an **online mutual learning** objective. Given training losses, the network dynamically selects targets:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{pose}} + \lambda_{\text{mutual}} \mathcal{L}_{\text{mutual}}(\pi_{\theta_{\text{in}}}, \pi_{\theta_{\text{out}}})$$

### Quantitative Performance Comparison

Our method achieved state-of-the-art results on major benchmarks:

| Dataset | Metric | Input Baseline | **HANet (Ours)** | Improvement |
|:---|:---|:---:|:---:|:---:|
| **Sub-JHMDB (2D)** | PCK @ 0.05 | 57.3% | **91.9%** | **+34.6%** |
| **Human3.6M (3D)** | MPJPE (mm) | 54.6mm | **52.8mm** | **-1.8mm** |
| **AIST++ (3D)** | MPJPE (mm) | 107.7mm | **69.2mm** | **-38.5mm** |
| **3DPW (SMPL)** | MPJPE (mm) | 78.9mm | **77.1mm** | **-1.8mm** |

---

### Resources
* **Paper:** [CVF Open Access Paper](https://openaccess.thecvf.com/content/WACV2023/html/Jin_Kinematic-Aware_Hierarchical_Attention_Network_for_Human_Pose_Estimation_in_WACV_2023_paper.html)
* **Code:** [GitHub Repository (KyungMinJin/HANet)](https://github.com/KyungMinJin/HANet)
</div>

