---
layout: post
title: "Cross-Modality Shared & Unique Information Factorization (SAMIF)"
title_ko: "교차 모달리티 공유 및 고유 정보 분리 학습 (SAMIF)"
author: Kyung-Min Jin
categories: [Machine-Learning]
tags: [Multimodal, Semantic-Segmentation, Cross-Attention]
image: assets/images/multimodal_samif.png
description: "A deep dive into Semantic-Aware Mutual Information Factorized Learning (SAMIF) for robust multimodal semantic segmentation."
description_ko: "멀티모달 시맨틱 세그멘테이션의 강건성 향상을 위해 공유 표현과 모달리티별 고유 표현을 분리하여 상호 정보량을 최적화하는 SAMIF 방법론을 설명합니다."
permalink: /posts/samif/
featured: false
hidden: false
rating: 4.8
---

<div class="lang-ko" markdown="1">
# 교차 모달리티 공유 및 고유 정보 분리 학습 (SAMIF)

멀티모달 학습(예: RGB 이미지와 깊이 맵, 열화상 이미지 또는 오디오 로그 결합)의 목적은 다양한 센서에서 제공되는 상호 보완적인 정보를 활용하는 것입니다. 그러나 단순한 융합 방식(예: 단순 연결(concatenation) 또는 더하기)은 서로 다른 모달리티가 **공유 정보**(중복)와 **고유 정보**(상호 보완)를 동시에 포함하고 있다는 사실을 무시하기 때문에 최적의 성능을 내지 못하는 경우가 많습니다.

본 포스트에서는 이러한 모달리티 표현을 분리하여 멀티모달 시맨틱 세그멘테이션 성능을 높이도록 설계된 **시맨틱 인지 상호 정보 분리 학습(Semantic-Aware Mutual Information Factorized Learning, SAMIF)** 프레임워크를 소개합니다.

---

## 1. 모달리티 표현의 인수분해 (Representation Factorization)

SAMIF는 각 모달리티 $M_i$의 표현을 두 개의 서로 다른 잠재 공간(latent spaces)으로 분해합니다:
1. **공유 표현 ($S$):** 모든 입력 모달리티에 공통적으로 포함된 정보 (예: RGB 이미지와 깊이 맵 모두에서 뚜렷이 드러나는 물체의 경계선).
2. **고유 표현 ($U_i$):** 해당 모달리티 $M_i$에만 독립적으로 존재하는 정보 (예: 열화상 이미지의 온도 패턴, 또는 RGB 이미지의 고주파 텍스처 디테일).

$$H_{M_i} = f_{\text{shared}}(M_i) \oplus f_{\text{unique}}(M_i)$$

---

## 2. 상호 정보량(Mutual Information) 최소화 및 최대화

이러한 분리를 유도하기 위해, PyTorch 학습 루프 내에 **상호 정보량(Mutual Information, MI)** 제약 조건을 설정합니다:

* **공유 표현과 고유 표현 간의 MI 최소화:** 고유 표현이 공유 표현의 정보를 포함하지 않도록 강제합니다:
  
  $$\min \mathcal{I}(S; U_i)$$

* **각 모달리티별 공유 표현 간의 MI 최대화:** 서로 다른 모달리티에서 추출된 공유 표현들이 서로 정렬(align)되도록 유도합니다:
  
  $$\max \mathcal{I}(S_1; S_2)$$

이 제약 조건들은 중간 feature 맵 단계에서 MINE과 같은 신경망 기반 상호 정보량 추정기나 대비 학습 손실 함수(InfoNCE Contrastive Loss)를 사용해 구현됩니다.

---

## 3. 교차 어텐션(Cross-Attention) 기반 feature 융합

분리된 feature들은 멀티헤드 **교차 어텐션(cross-attention)** 매커니즘을 통해 최종 융합됩니다:

```
[공유 feature S] ----------------\
                               +---> [교차 어텐션 융합] ---> [세그멘테이션 디코더]
[모달리티별 고유 feature U_i] ----/
```

이를 통해 네트워크는 공유 정보가 부족할 때에만 고유 feature에 동적으로 집중할 수 있게 되며, 일부 센서가 오작동하는 상황(예: 카메라 화면이 어두워져 열화상 센서의 고유 feature이 우선적으로 사용되는 경우)에서도 강건한 세그멘테이션 결과를 도출해 냅니다.

---

### 실험적 결과

표준 멀티모달 벤치마크 데이터셋에서 SAMIF 프레임워크는 다음 성과를 보여주었습니다:
* 평균 Intersection over Union (mIoU)에서 **2~3% 수준의 성능 향상**.
* 센서 신호 유실을 모사한 실험 환경에서 매우 뛰어난 강건성 입증 (단순 융합 베이스라인 대비 최대 15% 높은 mIoU 기록).
* 최종적으로 ONNX 포맷으로 변환되어 엣지 디바이스 내 Qualcomm Neural Processing SDK 환경에 성공적으로 배포 완료.
</div>

<div class="lang-en" markdown="1">
# Cross-Modality Shared & Unique Information Factorization (SAMIF)

In multimodal learning (e.g., combining RGB images with depth maps, thermal images, or audio logs), the goal is to leverage complementary information from different sensors. However, simple fusion methods (like concatenation or addition) often fail because they ignore the fact that different modalities contain both **shared** (redundant) and **unique** (complementary) information.

In this post, we introduce **Semantic-Aware Mutual Information Factorized Learning (SAMIF)**, a framework designed to factorize modality representations and improve multimodal semantic segmentation.

---

## 1. Modality Representation Factorization

SAMIF decomposes the representation of each modality $M_i$ into two distinct latent spaces:
1. **Shared Representation ($S$):** Features containing information that is common across all input modalities (e.g., object boundaries visible in both RGB and depth maps).
2. **Unique Representation ($U_i$):** Features containing information exclusive to modality $M_i$ (e.g., temperature patterns in thermal logs, or high-frequency texture details in RGB).

$$H_{M_i} = f_{\text{shared}}(M_i) \oplus f_{\text{unique}}(M_i)$$

---

## 2. Mutual Information Minimization & Maximization

To enforce this factorization, we utilize **Mutual Information (MI)** constraints during PyTorch training:

* **Minimizing MI between Shared and Unique:** We want the unique representations to contain no information about the shared features:
  
  $$\min \mathcal{I}(S; U_i)$$

* **Maximizing MI between Shared Representations:** We want the shared representations from different modalities to align:
  
  $$\max \mathcal{I}(S_1; S_2)$$

We implement these constraints using neural mutual information estimators (like MINE) or contrastive losses (InfoNCE) on the intermediate feature maps.

---

## 3. Cross-Attention Fusion

Once factorized, the features are fused using a multi-head **cross-attention** mechanism:

```
[Shared Features S] -------\
                            +---> [Cross-Attention Fusion] ---> [Segmentation Decoder]
[Unique Features U_i] -----/
```

This ensures the network dynamically attends to unique features only when the shared features are insufficient, yielding robust segmentation even under sensor failures (e.g., low-light camera conditions where thermal unique features take precedence).

---

### Experimental Results

On standard multimodal benchmarks, SAMIF achieved:
* **2-3% improvement** in mean Intersection over Union (mIoU).
* Significant robustness under simulated sensor dropouts (up to 15% better mIoU compared to vanilla fusion baselines).
* Successfully compiled to ONNX and deployed to Qualcomm neural processing SDK on edge devices.
</div>
