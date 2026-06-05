---
layout: post
title: "Cross-Modality Shared & Unique Information Factorization (SAMIF)"
author: Kyung-Min Jin
categories: [Machine-Learning]
tags: [Multimodal, Semantic-Segmentation, Cross-Attention]
image: assets/images/3.jpg
description: "A deep dive into Semantic-Aware Mutual Information Factorized Learning (SAMIF) for robust multimodal semantic segmentation."
featured: false
hidden: false
rating: 4.8
---

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
