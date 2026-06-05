---
layout: post
title: "[WACV 2023 Oral] Kinematic-aware Hierarchical Attention Network for Video Pose Estimation"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [WACV, Pose-Estimation, Attention, Deep-Learning]
image: assets/images/HANet.png
description: "A summary of our WACV 2023 Oral paper introducing a kinematic continuity-aware hierarchical attention network for video-based human pose estimation."
permalink: /posts/hanet/
featured: true
hidden: false
rating: 5.0
---

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

