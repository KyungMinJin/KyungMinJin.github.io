---
layout: post
title: "Modality-Aware Policy Optimization (GRPO) in Multimodal LLMs"
title_ko: "멀티모달 LLM에서의 모달리티 인지 정책 최적화 (GRPO)"
author: Kyung-Min Jin
categories: [Machine-Learning]
tags: [Reinforcement-Learning, VLM, Alignment, Deep-Learning]
image: assets/images/grpo_vlm_alignment.png
description: "Analyzing the math and efficiency gains of Group Relative Policy Optimization (GRPO) with modality-aware weighting for aligning vision-language models."
description_ko: "VLM 정렬을 위해 크리틱 네트워크를 제거하여 GPU 메모리 효율성을 극대화한 GRPO의 수학적 수식과 멀티모달 동적 가중치 설계 기법에 대해 알아봅니다."
permalink: /posts/grpo/
featured: true
hidden: false
rating: 4.9
---

<div class="lang-ko" markdown="1">
# 멀티모달 LLM에서의 모달리티 인지 정책 최적화 (GRPO)

강화학습을 통한 멀티모달 모델(VLM) 정렬(Alignment) 연구는 전통적으로 PPO(Proximal Policy Optimization) 알고리즘에 의존해 왔습니다. 하지만 PPO는 액터(Actor) 모델과 크기가 거의 동일한 **크리틱(Critic, Value) 네트워크**를 동시에 유지해야 합니다. 이는 대형 모델 학습 시 그래픽 메모리 제한으로 인해 배치 사이즈(batch size)를 크게 제약하는 병목 현상을 초래합니다.

DeepSeek에 의해 제안되고 최신 추론 모델 정렬에 널리 활용되고 있는 **GRPO(Group Relative Policy Optimization)**는 그룹 상대적 보상(group-relative rewards)을 활용함으로써 크리틱 네트워크를 완전히 제거합니다. 본 포스트에서는 GRPO의 수학적 공식화, 멀티모달 환경에서의 모달리티 인지 동적 가중치 기법, 그리고 학습 효율성을 분석합니다.

---

## 1. 크리틱 네트워크 없이 Advantage 계산하기

GRPO는 상태 가치 $V(s)$를 예측하는 크리틱 네트워크를 학습시키는 대신, 단일 질문(Prompt) $q$에 대해 현재 정책 모델로부터 $N$개의 대답 $\{o_1, o_2, \dots, o_N\}$을 무작위 샘플링합니다.

이후 샘플링된 그룹 내 보상값들의 평균과 표준편차를 기준으로 개별 대답 $o_i$의 상대적 우위(Advantage) $A_i$를 도출합니다:

$$A_i = \frac{r(q, o_i) - \text{mean}(R)}{\text{std}(R)}$$

여기서 $R = \{r(q, o_1), r(q, o_2), \dots, r(q, o_N)\}$ 입니다. 이렇게 계산된 상대적 Advantage는 PPO의 목적 함수(objective function) 내의 절대 가치 베이스라인을 직접 대체하게 됩니다:

$$\mathcal{L}_{\text{GRPO}}(\theta) = \frac{1}{N} \sum_{i=1}^N \min \left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)} A_i, \text{clip}\left(\frac{\pi_\theta(o_i|q)}{\pi_{\theta_{\text{old}}}(o_i|q)}, 1-\epsilon, 1+\epsilon\right) A_i \right) - \beta \mathbb{D}_{\text{KL}}(\pi_\theta || \pi_{\text{ref}})$$

이 방식은 크리틱 모델을 완전히 제거하여 학습을 대폭 단순화하고, GPU 메모리 요구량을 약 **30-40%** 감소시켜 동일 하드웨어 대비 배치 크기를 크게 늘릴 수 있습니다.

---

## 2. 모달리티 인지 동적 가중치 (Modality-Aware Online Weighting)

텍스트, 이미지, 오디오 등이 결합된 멀티모달 환경에서 모델은 텍스트 추론은 뛰어나지만 시각적 세부 사항 인식에는 약한 모습을 보이는 등 모달리티별로 불균성한 학습 결과를 낼 수 있습니다. 특정 모달리티에만 지나치게 최적화되는 경우 다른 모달리티 성능이 오히려 하락할 우려가 있습니다.

이를 방지하기 위해 **모달리티 인지 동적 가중치(modality-aware online weighting)** 기법을 도입합니다. 최종 보상 함수를 모달리티별 구성 요소로 분해합니다:

$$R_{\text{total}} = w_{\text{text}} R_{\text{text}} + w_{\text{vision}} R_{\text{vision}} + w_{\text{audio}} R_{\text{audio}}$$

학습 루프 중 각 모달리티의 이동 평균 보상 실적에 따라 가중치 $w_m$을 동적으로 업데이트하여, 특정 도메인에 편향된 오버피팅을 방지합니다. 가중치 갱신 공식은 다음과 같습니다:

$$w_m^{(t+1)} = \alpha w_m^{(t)} + (1-\alpha) \cdot \text{sigmoid}\left(\bar{R}_m^{(t)} - \mu_m\right)$$

여기서 $\alpha$는 모멘텀 하이퍼파라미터이며, $\mu_m$은 모달리티 $m$의 베이스라인 평균 성능 수준입니다.

---

## 3. 고속 추론 및 할루시네이션(Hallucination) 억제

강화학습을 통한 정렬 과정에서 자주 관측되는 부작용 중 하나는 **생각 과정(Chain-of-Thought, CoT)에서의 환각(Hallucination)** 현상입니다. 단계적 추론을 하도록 유도했을 때, 입력 이미지에 없는 시각적 feature들을 임의로 지어내는 현상이 나타납니다.

이 문제를 방지하기 위해 추론 경로상에서 환각 오류를 검출하는 보조 분류기(auxiliary classifier)를 활용하며, 이를 GRPO 보상 루프에 패널티 요인으로 차감 반영합니다:

$$r(q, o_i) = r_{\text{task}}(q, o_i) - \lambda_{\text{hal}} \cdot P_{\text{hallucination}}(o_i|q)$$

이러한 패널티 모델 적용을 통해 비합리적인 논리 전개를 차단함으로써 사실적 정확도(factual accuracy)를 최대 **20.7%** 향상시킬 수 있었습니다.

---

## 4. 구현 가이드라인

**veRL**이나 **TRL** 등의 강화학습 프레임워크 상에 GRPO VLM 정렬 알고리즘을 구축할 때의 유의사항입니다:
* **그룹 크기 ($N$):** 통상적으로 그룹 크기 $N$은 $4 \sim 8$ 사이를 유지합니다. $4$보다 작으면 Advantage 추정 오차가 지나치게 커지며, $8$보다 크면 매 스텝 샘플링 비용이 지나치게 증가합니다.
* **보상 설계 (Reward Mixing):** 바운딩 박스 내의 좌표 비교 등 규칙 기반(Rule-based) 보상과 시각적 일관성을 측정하는 모델 기반(Model-based) 보상을 함께 믹스하여 사용하는 것이 좋습니다.
</div>

<div class="lang-en" markdown="1">
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
</div>

