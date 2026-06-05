---
layout: post
title: "Robotic Perception & Natural Language Object Grounding via Knowledge Graphs"
title_ko: "지식 그래프를 활용한 로봇 인지 및 자연어 객체 그라운딩(Language Grounding)"
author: Kyung-Min Jin
categories: [Robotics]
tags: [Embodied-AI, Knowledge-Graph, RAG]
image: assets/images/robotics_perception_kg.png
description: "Exploring how robots can bridge visual perception and language understanding using structured Knowledge Graphs and Retrieval-Augmented Generation."
description_ko: "로봇이 구조화된 지식 그래프와 검색 증강 생성(RAG) 파이프라인을 활용하여 시각 정보와 자연어 명령어(객체 그라운딩)를 매핑하는 구조를 다룹니다."
permalink: /posts/robotics-kg/
featured: true
hidden: false
rating: 5.0
---

<div class="lang-ko" markdown="1">
# 지식 그래프를 활용한 로봇 인지 및 자연어 객체 그라운딩(Language Grounding)

로봇이 실제 인간의 주거 및 작업 환경에서 효과적으로 동작하기 위해서는 *"노트북 옆에 있는 커피 머그잔을 가져다줘"*와 같은 자연어 명령을 올바르게 이해할 수 있어야 합니다. 이 태스크를 **언어 그라운딩(Language Grounding)**이라고 하며, 문장 속 단어를 물리적 환경의 특정 객체, 공간적 관계 및 행동 양식과 매핑시키는 과정을 포함합니다.

본 포스트에서는 **공간 컨텍스트 지식 그래프(Knowledge Graphs)**와 **벡터 데이터베이스(Qdrant)**를 결합하여 강건한 객체 그라운딩 파이프라인을 구축하는 방법에 대해 논의합니다.

---

## 1. 공간적 및 시간적 객체 그라운딩의 한계

OWL-ViT나 Grounding DINO와 같은 최신 오픈 보카블러리(Open-Vocabulary) 객체 검출기들은 텍스트 입력을 바탕으로 실시간 객체를 잘 검출해 냅니다. 하지만 다음과 같은 한계가 존재합니다:
1. **시간적 지속성 부족 (Temporal Persistence):** 물체가 가려지거나 로봇의 현재 시야각(Field of View) 밖에 있는 경우, 여전히 방 안에 존재하는지를 기억하고 인지하는 능력이 결핍되어 있습니다.
2. **컨텍스트 연관성 결여 (Contextual Association):** *"내가 가장 아끼는 컵"*과 같이 과거 상호작용 역사에 의존적인 추상적인 개념을 직관적으로 매핑하지 못합니다.

---

## 2. 컨텍스트 지식 그래프의 구조 설계

이 문제를 해결하기 위해 로봇이 수집한 공간 정보를 동적 **지식 그래프 (Knowledge Graph, KG)** 형태로 표현합니다:

* **노드 (Nodes):** 물리적 객체(예: `Mug`, `Table`, `User`), 공간적 위치 구획(예: `Kitchen`), 혹은 추상적 속성(예: `색상: 파랑색`)을 나타냅니다.
* **엣지 (Edges):** 공간 관계(예: `위(on)`, `옆(next_to)`), 소유 관계(`소유주: 누구`), 혹은 과거 상태 로그를 기록합니다.

로봇은 환경을 이동하며 비주얼 센서로 취득한 시각 관측치를 기반으로 이 그래프 노드와 엣지를 실시간으로 업데이트합니다.

```
       [Mug: #042] ---(위에 있음)---> [Table: #001]
            |
       (소유주)
            v
       [User: 경민]
```

---

## 3. RAG 기반 하이브리드 질의 (Hybrid Querying)

사용자가 음성/자연어 명령을 내리면, **검색 증강 생성(Retrieval-Augmented Generation, RAG)** 파이프라인을 통해 공간 정보를 질의합니다:

1. **벡터 검색 (Qdrant):** 의미론적 설명에 따라 후보군을 1차 선별합니다 (예: 벡터 DB에서 *"머그잔"*을 검색).
2. **그래프 탐색 (LlamaIndex):** 그래프 연결 관계를 활용하여 후보군을 최종 필터링합니다 (예: `소유주: 경민`, `위치: 테이블 위` 조건을 만족하는 머그잔 필터링).
3. **LLM 추론 (LangChain):** LLM이 타겟 노드 정보를 취합하여 로봇 팔의 파지(manipulation) 정책에 넘겨줄 구체적인 물리 좌표를 생성해 냅니다.

벡터 데이터베이스와 구조화된 지식 그래프를 상호 보완적으로 활용함으로써, 로봇은 지극히 모호하고 정황 중심적인(context-dependent) 인간의 명령을 높은 신뢰도로 완수할 수 있게 됩니다.

---

## 4. 핵심 요약
구조화된 지식 그래프와 비주얼-언어 모델(VLM)의 통합은 Embodied 인공지능(Embodied AI) 에이전트가 현실 세계에 대한 인지 지도를 그릴 수 있게 해줍니다. 이 접근법은 기초적인 시각 인지 모델과 고차원 기호적 추론(Symbolic Reasoning) 모델 사이의 간극을 훌륭히 연결해 줍니다.
</div>

<div class="lang-en" markdown="1">
# Robotic Perception & Natural Language Object Grounding via Knowledge Graphs

For robots to operate effectively in human environments, they must understand natural language commands (e.g., *"Bring me the coffee mug next to the laptop"*). This task, known as **Language Grounding**, requires mapping words in a sentence to specific objects, spatial relationships, and actions in the physical world.

In this post, we discuss how we can build a robust object-grounding pipeline using a combination of **contextual Knowledge Graphs** and **Vector Databases (Qdrant)**.

---

## 1. The Challenge of Spatial and Temporal Object Grounding

Modern Open-Vocabulary Object Detectors (like OWL-ViT or Grounding DINO) can detect objects based on text queries. However, they lack:
1. **Temporal Persistence:** Knowing if an object is still in the room when it is currently occluded or out of the robot's field of view.
2. **Contextual Association:** Understanding abstract concepts (e.g., *"my favorite mug"*) which depend on historical interaction context.

---

## 2. Construction of a Contextual Knowledge Graph

To address this, we represent the robot's environment as a dynamic **Knowledge Graph (KG)**:

* **Nodes** represent physical entities (e.g., `Mug`, `Table`, `User`), spatial regions (e.g., `Kitchen`), or abstract properties (e.g., `Color: Blue`).
* **Edges** represent spatial relations (e.g., `on`, `next_to`), owner relations (`owned_by`), or status logs.

As the robot navigates the room, it continuously updates the nodes and edges based on its visual observations.

```
       [Mug: #042] ---(on)---> [Table: #001]
            |
      (owned_by)
            v
       [User: Kyung-Min]
```

---

## 3. RAG-Based Hybrid Querying

When the user gives a command, we utilize a **Retrieval-Augmented Generation (RAG)** pipeline to query the environment:

1. **Vector Search (Qdrant):** We retrieve candidates based on semantic descriptions (e.g., search vector DB for *"mug"*).
2. **Graph Traversal (LlamaIndex):** We filter candidates using graph relationships (e.g., filter for the mug that has the relationship `owned_by: Kyung-Min` and `on: Table`).
3. **LLM Reasoning (LangChain):** An LLM synthesizes the target node information and outputs actionable coordinates for the robot's manipulation policy.

By combining vector databases with structured graphs, robots can resolve highly ambiguous, context-dependent requests with superior reliability.

---

### Key Takeaway
Integrating structured knowledge graphs with vision-language models allows embodied agents to build a cognitive map of the world. This approach bridges the gap between raw visual perception and high-level symbolic reasoning.
</div>
