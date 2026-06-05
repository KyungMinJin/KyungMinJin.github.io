---
layout: post
title: "GRPO: Group Relative Policy Optimization for Efficient VLM Alignment"
author: Kyung-Min Jin
categories: [Machine-Learning]
tags: [Reinforcement-Learning, VLM, Alignment]
image: assets/images/grpo_vlm_alignment.png
description: "Analyzing the math and efficiency gains of Group Relative Policy Optimization (GRPO) for aligning vision-language models."
featured: true
hidden: false
rating: 4.9
---

# GRPO: Group Relative Policy Optimization for Efficient VLM Alignment

Aligning Vision-Language Models (VLMs) using Reinforcement Learning has traditionally relied on PPO (Proximal Policy Optimization). However, PPO requires a secondary **critic (value) network** that is often as large as the actor network itself. This severely constrains the batch size and increases GPU memory requirements during training.

**Group Relative Policy Optimization (GRPO)**, introduced by DeepSeek and popular in modern reasoning models, eliminates the critic network by using group-relative rewards. In this post, we explore its mathematical formulation and deployment benefits for VLM alignment.

---

## 1. How GRPO Eliminates the Critic Network

Instead of training a critic network to estimate the baseline value $V(s)$, GRPO samples a group of $N$ outputs $\{o_1, o_2, \dots, o_N\}$ for a single input prompt $q$ using the reference policy.

The advantage $A_i$ of each output $o_i$ is computed by normalizing the rewards within the sampled group:

$$A_i = \frac{r(q, o_i) - \text{mean}(R)}{\text{std}(R)}$$

Where $R = \{r(q, o_1), r(q, o_2), \dots, r(q, o_N)\}$. This relative advantage replaces the absolute value baseline in the PPO objective:

$$\mathcal{L}_{\text{GRPO}}(\theta) = \frac{1}{N} \sum_{i=1}^N \min \left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)} A_i, \text{clip}\left(\frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)}, 1-\epsilon, 1+\epsilon\right) A_i \right) - \beta \mathbb{D}_{\text{KL}}(\pi_\theta || \pi_{\text{ref}})$$

---

## 2. Benefits for Multimodal Alignment

In Multimodal Large Language Models (MLLMs), VLM outputs are extremely high-dimensional due to long CoT (Chain-of-Thought) visual grounding paths. GRPO is highly beneficial here for two reasons:

1. **Memory Reduction:** Eliminating the value network saves roughly **30-40% of active GPU memory**, allowing for larger batch sizes or longer sequence lengths (essential for visual reasoning tasks).
2. **Relative Comparison:** It is often easier to determine which VLM output is *better* compared to others in a group (e.g. which output has fewer hallucinations) than assigning an absolute quality score via a value model.

---

## 3. Implementation Notes

When deploying GRPO for VLM alignment on frameworks like **veRL** or **TRL**:
* Keep group size $N$ between $4$ and $8$. A smaller group size degrades advantage estimation quality, while larger group sizes increase sampling overhead.
* Use a mix of rule-based reward functions (e.g., matching coordinates in a bounding box) and model-based reward functions (e.g., visual coherence score) to build a robust reward loop.
