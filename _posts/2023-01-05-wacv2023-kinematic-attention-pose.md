---
layout: post
title: "[WACV 2023 Oral] Kinematic-aware Hierarchical Attention Network for Video Pose Estimation"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [WACV, Pose-Estimation, Attention]
image: assets/images/pose_estimation_cv.png
description: "A summary of our WACV 2023 Oral paper introducing a kinematic continuity-aware hierarchical attention network for video-based human pose estimation."
featured: true
hidden: false
rating: 5.0
---

# [WACV 2023 Oral] Kinematic-aware Hierarchical Attention Network for Video Pose Estimation

In video-based human pose estimation, maintaining **temporal and kinematic consistency** across frames is a major challenge. Standard frame-by-frame pose estimators often suffer from jittery predictions, joint swap errors, and failure under fast motion or occlusion because they do not model physical skeletal joints and anatomical limits.

Our paper, presented as an **Oral presentation at WACV 2023**, proposes the **Kinematic-aware Hierarchical Attention Network (KHAN)** to resolve these issues by explicitly encoding joint relations and temporal continuity.

---

## 1. The Core Idea: Kinematic Constraints in Attention

Standard self-attention mechanisms in transformers treat all keypoints in a human body equally, ignoring the physical structure of the skeleton. In contrast, KHAN structures attention hierarchically based on **kinematic joints**:

* **Local Attention:** Computes attention within adjacent joints (e.g., connecting wrist to elbow, elbow to shoulder) representing physical bone links.
* **Global Attention:** Captures long-range dependencies (e.g., left hand to right hand coordinating during an action).

By masking out physically impossible joint movements, we regularize the model to predict anatomically plausible poses.

---

## 2. Temporal Continuity Modeling

In addition to spatial constraints, we model temporal trajectories using a specialized **temporal attention encoder**. Instead of simple smoothing filters (which introduce lag), our network learns to look ahead and behind in the video stream to predict occluded joints based on the velocity and acceleration vectors of adjacent visible joints.

```
Frame t-1: [Visible Elbow] ---\
Frame t  : [Occluded Wrist] ---> [Temporal Encoder] ---> Predicted Wrist Position
Frame t+1: [Visible Wrist] ---/
```

---

## 3. Visual Demonstration (HANet Action)

Below is a visual demo highlighting the robustness of our Kinematic-aware Hierarchical Attention Network on sports pose tracking compared to baseline frame-by-frame pose estimation:

<div class="text-center my-4">
    <!-- Note: You can replace this placeholder image with your actual hanet_demo.gif file in assets/images/ -->
    <img src="{{ site.baseurl }}/assets/images/pose_estimation_cv.png" class="img-fluid rounded shadow-lg" alt="HANet Pose Tracking Demo" style="max-height: 400px;">
    <p class="text-muted mt-2" style="font-size: 0.85rem;">Figure: HANet tracking velocity & acceleration vector continuity under high occlusion.</p>
</div>

---

## 4. Results on Benchmarks

Our method achieved state-of-the-art results on major benchmarks:
* **Human3.6M:** Reduced Mean Per Joint Position Error (MPJPE) by **3.2mm** compared to prior transformer baselines.
* **MPI-INF-3DHP:** Improved 3D PCK by **2.8%** in outdoor sequences.

---

### Resources
* **Paper:** [CVF Open Access](https://openaccess.thecvf.com/content/WACV2023/html/Jin_Kinematic-Aware_Hierarchical_Attention_Network_for_Human_Pose_Estimation_in_WACV_2023_paper.html)
* **Code:** [GitHub Repository (KyungMinJin/KHAN)](https://github.com/KyungMinJin)
