---
layout: post
title: "Modality-Aware Policy Optimization (GRPO) in Multimodal LLMs"
author: Kyung-Min Jin
categories: [Notes]
tags: [RL, VLM]
image: assets/images/10.jpg
description: "A summary of recent research on applying Group Relative Policy Optimization (GRPO) for multimodal models, optimizing reasoning speed and accuracy."
featured: false
hidden: false
rating: 5.0
---

# Modality-Aware Policy Optimization (GRPO) in Multimodal LLMs

Reinforcement Learning from Human Feedback (RLHF) and related policy optimization methods (like DPO, GRPO) have become standard for alignment in Large Language Models. However, when adapting these to Multimodal Large Language Models (MLLMs), we face unique challenges due to disparate modal representations (e.g., text, vision, audio).

In this note, we examine the integration of Group Relative Policy Optimization (GRPO) for training multimodal assistants, focusing on **modality-aware online weighting** and **fast reasoning**.

---

## 1. Group Relative Policy Optimization (GRPO) Overview

Unlike standard PPO which requires a separate critic network to estimate state values, **GRPO** computes the baseline relative to a group of sampled outputs for a single prompt. For each prompt $q$, we sample $N$ outputs $\{o_1, o_2, \dots, o_N\}$ from the old policy $\pi_{\theta_{old}}$. 

The reward $r(q, o_i)$ for each output is computed, and the relative advantage $A_i$ is normalized within the group:

$$A_i = \frac{r(q, o_i) - \text{mean}(R)}{\text{std}(R)}$$

This simplifies the training pipeline significantly, reducing GPU memory footprint because no separate value model (critic) is needed.

---

## 2. Modality-Aware Online Weighting

In multimodal environments, a model might perform exceptionally well on textual reasoning but fail at grounding physical or visual details. 

To resolve this, we can apply **modality-aware online weighting**. The reward function is decomposed into modal components:

$$R_{\text{total}} = w_{\text{text}} R_{\text{text}} + w_{\text{vision}} R_{\text{vision}} + w_{\text{audio}} R_{\text{audio}}$$

By dynamically updating the weights $w_m$ based on the moving average of group performance on each modality, we prevent the model from over-optimizing for one modality at the expense of others.

---

## 3. Fast Reasoning & Hallucination Prevention

A common failure mode of MLLMs under RL alignment is **hallucination in chain-of-thought (CoT)**. When the model is encouraged to think step-by-step, it sometimes hallucinates visual details that are not present in the input image.

To mitigate this, we train a small helper classifier that predicts missed or hallucinated cases in the reasoning path. The prediction score is fed back into the GRPO reward loop as a penalty factor, successfully boosting factual accuracy by up to **20.7%**.

---

### References
1. Verma et al., "MAPLE: Modality-Aware Post-training and Learning Ecosystem," arXiv preprint, 2026.
2. Shao et al., "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models," arXiv, 2024.
