---
layout: post
title: "Quantization-Aware Training (QAT) for Edge Pose Estimation"
author: Kyung-Min Jin
categories: [Computer-Vision]
tags: [Quantization, Edge-AI, Pose-Estimation]
image: assets/images/qat_pose_estimation.png
description: "How to use Quantization-Aware Training (QAT) to preserve keypoint accuracy when deploying pose estimation models to low-power edge hardware."
permalink: /posts/qat/
featured: false
hidden: false
rating: 4.7
---

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
