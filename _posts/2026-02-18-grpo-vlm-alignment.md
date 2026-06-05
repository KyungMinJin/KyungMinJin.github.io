---
layout: post
title: "Modality-Aware Policy Optimization (GRPO) in Multimodal LLMs"
author: Kyung-Min Jin
categories: [Machine-Learning]
tags: [Reinforcement-Learning, VLM, Alignment, Deep-Learning]
image: assets/images/grpo_vlm_alignment.png
description: "Analyzing the math and efficiency gains of Group Relative Policy Optimization (GRPO) with modality-aware weighting for aligning vision-language models."
permalink: /posts/grpo/
featured: true
hidden: false
rating: 4.9
---

# Modality-Aware Policy Optimization (GRPO) in Multimodal LLMs

Aligning Vision-Language Models (VLMs) using Reinforcement Learning has traditionally relied on PPO (Proximal Policy Optimization). However, PPO requires a secondary **critic (value) network** that is often as large as the actor network itself. This severely constrains the batch size and increases GPU memory requirements during training.

**Group Relative Policy Optimization (GRPO)**, introduced by DeepSeek and popular in modern reasoning models, eliminates the critic network by using group-relative rewards. In this post, we explore its mathematical formulation, modality-aware online weighting, and deployment benefits for VLM alignment.

---

## 1. How GRPO Eliminates the Critic Network

Instead of training a critic network to estimate the baseline value $V(s)$, GRPO samples a group of $N$ outputs $\{o_1, o_2, \dots, o_N\}$ for a single input prompt $q$ using the reference policy.

The advantage $A_i$ of each output $o_i$ is computed by normalizing the rewards within the sampled group:

$$A_i = \frac{r(q, o_i) - \text{mean}(R)}{\text{std}(R)}$$

Where $R = \{r(q, o_1), r(q, o_2), \dots, r(q, o_N)\}$. This relative advantage replaces the absolute value baseline in the PPO objective:

$$\mathcal{L}_{\text{GRPO}}(\theta) = \frac{1}{N} \sum_{i=1}^N \min \left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)} A_i, \text{clip}\left(\frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)}, 1-\epsilon, 1+\epsilon\right) A_i \right) - \beta \mathbb{D}_{\text{KL}}(\pi_\theta || \pi_{\text{ref}})$$

This relative comparison model simplifies training, reducing GPU memory footprint by roughly **30-40%** and allowing for larger batch sizes.

---

## 2. Modality-Aware Online Weighting

In multimodal environments (e.g., combining text, image, and audio inputs), a model might perform exceptionally well on textual reasoning but fail at grounding physical or visual details. Over-optimization in a single modality can lead to degradation in others.

To resolve this, we apply **modality-aware online weighting**. The reward function is decomposed into modal components:

$$R_{\text{total}} = w_{\text{text}} R_{\text{text}} + w_{\text{vision}} R_{\text{vision}} + w_{\text{audio}} R_{\text{audio}}$$

By dynamically updating the weights $w_m$ based on the moving average of group performance on each modality, we prevent the model from over-optimizing for one modality at the expense of others. The weight updates are formulated as:

$$w_m^{(t+1)} = \alpha w_m^{(t)} + (1-\alpha) \cdot \text{sigmoid}\left(\bar{R}_m^{(t)} - \mu_m\right)$$

where $\alpha$ is a momentum hyperparameter and $\mu_m$ is the baseline average performance for modality $m$.

---

## 3. Fast Reasoning & Hallucination Prevention

A common failure mode of MLLMs under RL alignment is **hallucination in chain-of-thought (CoT)**. When the model is encouraged to think step-by-step, it sometimes hallucinates visual details that are not present in the input image.

To mitigate this, we train a auxiliary classifier that predicts missed or hallucinated cases in the reasoning path. The prediction score is fed back into the GRPO reward loop as a penalty factor:

$$r(q, o_i) = r_{\text{task}}(q, o_i) - \lambda_{\text{hal}} \cdot P_{\text{hallucination}}(o_i|q)$$

This penalty successfully boosts factual accuracy by up to **20.7%**, suppressing incorrect logical paths during search.

---

## 4. Implementation Notes

When deploying GRPO for VLM alignment on frameworks like **veRL** or **TRL**:
* **Group Size ($N$):** Keep group size $N$ between $4$ and $8$. A smaller group size degrades advantage estimation quality, while larger group sizes increase sampling overhead.
* **Reward Mixing:** Use a mix of rule-based reward functions (e.g., matching coordinates in a bounding box) and model-based reward functions (e.g., visual coherence score) to build a robust reward loop.

