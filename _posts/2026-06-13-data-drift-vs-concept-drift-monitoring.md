---
layout: post
title: "Practical Strategies for Detecting and Handling Data Drift vs. Concept Drift"
title_ko: "실무 관점의 Data Drift vs Concept Drift 탐지 및 대응 전략"
author: Kyung-Min Jin
categories: [MLOps]
tags: [Data-Drift, Concept-Drift, Model-Monitoring, MLOps]
image: assets/images/qat_pose_estimation.png
description: "A practical guide to understanding, detecting, and mitigating data drift and concept drift in production machine learning systems."
description_ko: "프로덕션 기계학습 시스템에서 발생하는 데이터 드리프트와 컨셉 드리프트를 탐지하고 해결하기 위한 실무적인 통계적 방법론과 시스템 설계 방법을 다룹니다."
permalink: /posts/drift-monitoring-strategies/
featured: false
hidden: false
rating: 4.9

published: false
---

<div class="lang-ko" markdown="1">
# 실무 관점의 Data Drift vs Concept Drift 탐지 및 대응 전략

딥러닝 모델을 프로덕션 환경에 배포한 직후에는 높은 정확도를 보이지만, 시간이 지나면서 성능이 점차 저하되는 현상을 겪게 됩니다. 이는 학습 데이터의 분포와 실제 운영 환경의 데이터 분포가 달라지기 때문입니다. 이 현상은 크게 **데이터 드리프트(Data Drift)**와 **컨셉 드리프트(Concept Drift)**로 나뉩니다. 

본 포스트에서는 실무에서 정답 레이블(Ground Truth)의 획득 속도를 고려하여 이 두 가지 드리프트를 어떻게 탐지하고, 운영 안정성을 확보하기 위해 어떻게 대응해야 하는지 설계 관점에서 설명합니다.

---

## 1. Data Drift vs. Concept Drift 핵심 비교

| 구분 | 데이터 드리프트 (Data Drift / Input Drift) | 컨셉 드리프트 (Concept Drift / Relation Drift) |
| :--- | :--- | :--- |
| **변화 요인** | 입력 데이터의 분포 변화 ($P(X)$의 변화) | 입력 데이터와 정답 간의 관계 변화 ($P(Y \vert X)$의 변화) |
| **정답 규칙** | 기존의 분류/예측 규칙은 동일하게 유지됨 | 기존 분류/예측의 기준 및 관계 자체가 모호해지거나 바뀜 |
| **제조/비전 예시** | 카메라 각도 변경, 작업장 조명 변화, 센서 노이즈 증가 | 신규 결함 유형 등장, 고객사 검사 스펙 상향 (Pass/Fail 기준 변경) |
| **탐지 시점** | **실시간/단기적 탐지 가능** (라벨 없이 통계 지표로 감지) | **중장기적 탐지** (정답 라벨이 확보되거나 피드백이 와야 감지) |
| **대응 전략** | 전처리 보정, Normalization 재설계, 데이터 증강 및 재학습 | 라벨 재정의, 모델 구조 변경, 경량 파인튜닝 또는 전면 재학습 |

---

## 2. 데이터 드리프트 (Data Drift) 탐지 방법론

제조 공정이나 실시간 서비스 환경에서는 정답 라벨($Y$)이 즉시 확보되지 않는 경우가 대부분입니다. 따라서 입력 데이터($X$) 또는 모델의 예측 값(이상치 점수 등)의 분포 변화를 모니터링하여 성능 하락을 선제적으로 예측해야 합니다.

### ① 실시간 모니터링: Anomaly Score Mean / Variance 탐지
가장 가볍고 빠르게 시스템의 변화를 감지하는 방법은 모델이 출력하는 **연속적인 점수(Score) 분포의 평균과 분산**을 모니터링하는 것입니다.
* **학습 시 baseline**: 평균 $\mu_0$, 표준편차 $\sigma_0$
* **최근 슬라이딩 윈도우(예: 최근 1시간)**: 평균 $\mu_t$, 표준편차 $\sigma_t$
* **평균 변화 트리거**: $\vert \mu_t - \mu_0 \vert > \alpha \cdot \sigma_0$ (일반적으로 $\alpha = 3$ 설정)
* **분산 변화 트리거**: $\frac{\sigma_t^2}{\sigma_0^2} > \beta$

### ② 통계적 분포 비교 기법 (주기적 배치 모니터링)
하루 혹은 일주일 단위의 배치 모니터링에서는 두 데이터 분포가 통계적으로 동일한지 비교하는 검정을 수행합니다.

* **KS Test (Kolmogorov-Smirnov Test)**
  * 두 누적분포함수(CDF) 간의 최대 거리($D$)를 측정합니다.
  * 비모수적(Non-parametric) 검정으로 분포 가정이 없으며 단일 연속형 변수(예: 센서 로그 단일 채널) 모니터링에 적합합니다.
  * p-value가 특정 임계값(예: 0.05) 이하로 떨어질 경우 Drift로 판정합니다.

* **PSI (Population Stability Index)**
  * 분포를 구간(Bin) 단위로 쪼개어 변화량을 측정합니다. 실무에서 가장 직관적인 대시보드 리포팅 지표입니다.
  * $PSI = \sum_{i} (P_i - Q_i) \ln\left(\frac{P_i}{Q_i}\right)$ (여기서 $P$는 Baseline 비율, $Q$는 대상 데이터 비율)
  * **해석 기준**: $PSI < 0.1$ (안정), $0.1 \le PSI < 0.25$ (미세한 드리프트), $PSI \ge 0.25$ (심각한 드리프트, 재학습 필요).

* **Wasserstein Distance (EMD - Earth Mover's Distance)**
  * 하나의 확률 분포를 다른 분포로 이동하는 데 필요한 최소 비용을 계산합니다.
  * 평균은 같지만 분포의 형태(Shape)가 변하는 Gradual Drift 감지에 뛰어납니다. 다만, 계산 비용이 비교적 높습니다.

---

## 3. 컨셉 드리프트 (Concept Drift) 탐지 및 대응

컨셉 드리프트는 입력 데이터의 형태가 변하지 않더라도, $X \to Y$ 매핑 기준이 바뀌기 때문에 모델 출력 점수만으로는 알아채기 어렵습니다.

### 탐지 기법
* **지연된 Ground Truth 수집 및 성능 모니터링**: 주기적으로 현업 작업자가 라벨링한 실제 데이터를 수집하여 Accuracy, Precision, Recall 등의 성능 하락 폭을 직접 모니터링합니다.
* **실패 케이스(Failure Cases) 분석**: 오탐이나 미탐이 급증할 때, 현업 검사원들이 피드백을 주는 로그를 분석하여 새로운 컨셉(예: 신규 스크래치 불량 기준)이 정의되었는지 분류합니다.

### 대응 파이프라인 설계
1. **Human-in-the-Loop 피드백 루프**: 현업에서 모호하다고 판정하여 수동 조치한 로그 데이터를 자동으로 수집 대상 플래그로 지정합니다.
2. **경량 파인튜닝 (LoRA / Adapter)**: 컨셉이 국소적으로 바뀐 경우(예: 특정 공정 라인 전용 가이드 추가), 전체 가중치를 다시 학습하기보다 LoRA(Low-Rank Adaptation)나 어댑터를 활용해 가벼운 미세조정만을 수행하여 배포 비용을 최소화합니다.
3. **규칙 기반 Fallback 설계**: 모델의 예측 신뢰도(Confidence Score)가 경계선(Threshold) 근처에 분포하는 경우, 강제로 수동 검사 단계로 넘기거나 기존의 룰베이스 코드로 분기 처리를 해주는 안전장치를 마련합니다.

---

## 4. 모니터링 아키텍처 요약

```
[실시간 추론] ──> 이미지/센서 데이터 ──> 모델 추론 ──> [Threshold 판정] ──> 결과 저장
                      │                                    │
                      ▼ (Raw Data)                         ▼ (Score)
              [Feature 저장소]                     [실시간 모니터링 (Mean/Var)] ──> Soft Alert
                      │                                    │
                      ▼ (Daily Batch)                      ▼ (Weekly Batch)
              [PSI / KS-Test 검정]                 [Retraining Pipeline 트리거]
```

성공적인 MLOps는 완벽한 성능의 단일 모델을 배포하는 것보다, **지속적으로 데이터의 흐름을 관측하고 이상 징후를 스스로 감지하여 대응할 수 있는 안전장치 시스템**을 구축하는 것에 있습니다.
</div>

<div class="lang-en" markdown="1">
# Practical Strategies for Detecting and Handling Data Drift vs. Concept Drift

Machine learning models often show high accuracy immediately after deployment to production, but experience a gradual decline in performance over time. This performance degradation occurs because the distribution of production data diverges from the training data distribution. This phenomenon is broadly classified into **Data Drift** and **Concept Drift**.

This post explores how to detect these two types of drift in real-world scenarios—taking into account the availability of ground truth labels—and outlines system architectures for maintaining model stability.

---

## 1. Key Comparison: Data Drift vs. Concept Drift

| Dimension | Data Drift (Input Drift) | Concept Drift (Relation Drift) |
| :--- | :--- | :--- |
| **Driver of Change** | Shift in input data distribution ($P(X)$ changes) | Shift in relationship between inputs and labels ($P(Y \vert X)$ changes) |
| **Decision Rule** | Existing classification/prediction rules remain valid | Rules or criteria for prediction become ambiguous or change entirely |
| **Manufacturing/CV Example** | Camera angle shifts, factory lighting changes, sensor noise increases | New defect categories emerge, customer inspection specs tighten (Pass/Fail criteria change) |
| **Detection Timing** | **Real-time / Short-term** (Can be detected using statistical metrics without labels) | **Medium to Long-term** (Requires ground truth labels or manual feedback to detect) |
| **Mitigation Strategy** | Preprocessing adjustments, normalization redesign, data augmentation & retraining | Label re-definition, model architecture modification, lightweight fine-tuning or full retraining |

---

## 2. Methodologies for Detecting Data Drift

In manufacturing pipelines or real-time service environments, ground truth labels ($Y$) are rarely available immediately. Therefore, we must monitor distribution shifts in input features ($X$) or model outputs (such as anomaly scores) to proactively predict performance drops.

### ① Real-Time Monitoring: Anomaly Score Mean / Variance Detection
The most lightweight way to monitor system shifts in real-time is by observing the **mean and variance of continuous prediction scores** over a sliding window.
* **Training Baseline**: Mean $\mu_0$, Standard Deviation $\sigma_0$
* **Recent Sliding Window (e.g., last 1 hour)**: Mean $\mu_t$, Standard Deviation $\sigma_t$
* **Mean Drift Trigger**: $\vert \mu_t - \mu_0 \vert > \alpha \cdot \sigma_0$ (typically $\alpha = 3$)
* **Variance Drift Trigger**: $\frac{\sigma_t^2}{\sigma_0^2} > \beta$

### ② Statistical Distribution Comparison (Periodic Batch Monitoring)
For daily or weekly batch monitoring, statistical hypothesis tests can determine if the production data matches the baseline training distribution.

* **KS Test (Kolmogorov-Smirnov Test)**
  * Measures the maximum distance ($D$) between the cumulative distribution functions (CDFs) of two samples.
  * As a non-parametric test, it makes no distribution assumptions and is ideal for continuous 1D variables (e.g., a single sensor log channel).
  * A drift is flagged if the p-value falls below a threshold (e.g., 0.05).

* **PSI (Population Stability Index)**
  * Measures the extent of shift by binning the distributions. This is the most popular metric for business-facing dashboards.
  * $PSI = \sum_{i} (P_i - Q_i) \ln\left(\frac{P_i}{Q_i}\right)$ (where $P$ is the baseline and $Q$ is the target dataset fraction).
  * **Thresholds**: $PSI < 0.1$ (stable), $0.1 \le PSI < 0.25$ (moderate shift), $PSI \ge 0.25$ (significant shift, retraining required).

* **Wasserstein Distance (EMD - Earth Mover's Distance)**
  * Measures the minimum cost of shifting one probability distribution to resemble another.
  * Excellent for detecting gradual drifts where the mean remains static but the shape of the distribution changes. However, it is computationally expensive.

---

## 3. Detecting and Mitigating Concept Drift

Because concept drift alters the mapping from $X \to Y$ without necessarily changing the characteristics of $X$ itself, it cannot be identified by looking at input feature metrics or raw model outputs alone.

### Detection Techniques
* **Delayed Ground Truth Auditing**: Periodically collect samples manually labeled by human operators to directly calculate performance metrics like Accuracy, Precision, and Recall.
* **Failure Case Categorization**: When false positives or false negatives spike, analyze feedback logs from operators to identify if a new concept (e.g., a new scratch defect standard) has been introduced.

### Mitigation Pipeline Design
1. **Human-in-the-Loop Feedback Loops**: Automatically flag cases manually overridden by operators and collect them for future training.
2. **Lightweight Fine-Tuning (LoRA / Adapters)**: When drift is localized (e.g., changes specific to a single factory line), avoid full retraining. Instead, deploy lightweight adapters like LoRA to reduce update overhead and deployment costs.
3. **Rule-Based Fallbacks**: If the model prediction confidence falls near the decision boundary (threshold), route the input to human operators or fall back to legacy rule-based heuristics.

---

## 4. Monitoring Architecture Overview

```
[Real-time Inference] ──> Image/Sensor Data ──> Model Inference ──> [Threshold Decision] ──> Save Results
                              │                                         │
                              ▼ (Raw Data)                              ▼ (Score)
                      [Feature Store]                        [Real-time Monitoring (Mean/Var)] ──> Soft Alert
                              │                                         │
                              ▼ (Daily Batch)                           ▼ (Weekly Batch)
                      [PSI / KS-Test Verification]           [Trigger Retraining Pipeline]
```

Successful MLOps is not about deploying a single "perfect" model; it is about building a **continuous observation system that autonomously detects anomalies and mitigates degradation**.
</div>
