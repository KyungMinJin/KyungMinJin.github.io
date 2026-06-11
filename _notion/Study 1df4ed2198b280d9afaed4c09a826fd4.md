# Study

# ETL 공부

## **Ch1. 빅데이터의 기초 지식**

### **[1] 빅데이터의 정착 (배경)**

- Hadoop, NoSQL -> Cloud, Data Warehouse, BI Tool -> Stream, AdHoc
- 빅데이터 << 처리를 통한 가치 창조
- 저장된 데이터는 Hadoop으로 모이고 그곳에서 대규모 데이터 처리가 실행됨
- Hadoop : 다수의 컴퓨터에서의 대량의 데이터 처리
- Hive : SQL 같은 쿼리 언어를 Hadoop에서 실행하기 위한 소프트웨어
- NoSQL DB : 빈번한 읽기/쓰기 및 분산 처리에 강점 : dict, json 등의 데이터 구조로 저장

엔터프라이즈 데이터 웨어하우스 (데이터 분석 기반)

- 대용량의 데이터 처리는 Hadoop으로 처리하고 적은 양의 중요한 데이터만 데이터 웨어하우스에 저장

데이터 디스커버리(데이터 웨어하아스에 저장된 데이터 시각화 방법) == BI(Bisuness Intelligence tool) : 셀프서비스용 BI 도구

2013년 이후 효율성, 편리성을 위한 Apache Spark 등장

### **[2] 빅데이터 시대의 데이터 분석 기반**

빅데이터 기술 : 다수의 분산 시스템을 조합하여 확장성이 뛰어난 데이터 처리 구조 만듦

- 데이터 파이프라인 : 데이터 수집 ~ 워크플로 관리
- 데이터 수집 : 벌크 형과 스트리밍 형의 데이터 전송
    - 벌크 형 : 이미 어딘가에 존재하는 데이터를 정리하여 추출하는 방법(정기적 데이터 수집)
    - 스트리밍 형 : 차례차례로 생성되는 데이터를 끊임없이 계속해서 보내는 방법

스트림 처리 & 배치 처리

- 스트림 처리(stream processing) : 스트리밍 형 방법으로 전달받은 데이터를 실시간으로 처리하는 방법
    - 기존에는 시계열 데이터베이스와 같은 실시간 처리 지향 데이터베이스를 사용
    - 1년간의 데이터 분석 : 스트림 처리는 장기적인 데이터 분석에 적합하지 않음. => 배치 처리(batch processing) : 어느정도 정리된 데이터를 효율적으로 가공하기 위함

분산 스토리지 : 객체 스토리지, NoSQL DB

수집된 데이터는 분산 스토리지에 저장됨(여러 컴퓨터와 디스크로 구성된 스토리지 시스템)

객체 스토리지 : 한 덩어리로 모인 데이터에 이름을 부여해서 파일로 저장.(ex. Amazon S3)

No SQL DB : APP에서 많은 데이터를 Read, Write하는 경우 성능 우수.

분산 데이터 처리 : 쿼리 엔진, ETL 프로세스

분산 스토리지에 저장된 데이터 처리에는 분산 데이터 처리(distribute data processing) 프레임워크 필요 => 나중에 분석하기 쉽도록 데이터를 가공해서 그 결과를 외부 데이터베이스에 저장하는 것

SQL을 통한 집계

1) 쿼리 엔진 도입 : Hive, 대화형 쿼리 엔진(interactive query engine)

2) 외부의 데이터 웨어하우스 제품 사용 by ETL Process(Extract-transform-load) : 다른 DB로 옮기기 위해 형변환 시키는 과정

ETL : 데이터베이스의 바깥에서 데이터를 가공하는 경우

ELT : 데이터를 읽은 후에 가공하는 경우

데이터 웨어하우스와 데이터 마트 : 데이터 파이프라인 기본형

데이터 웨어하우스는 대량의 데이터를 장기 보존하는 것에 최적화 되어있음 but 소량의 데이터를 다루는 것에서는 적합하지 않음

=> 데이터 마트 : 데이터 웨어하우스에 대한 과부화를 피하고, 데이터 분석과 같은 목적에 사용하는 경우에 웨어하우스에서 필요한 데이터만 추출하여 구축한 것

RDB, 로그 등을 저장하는 파일 서버 : 데이터 소스

ETL 프로세스를 통해 해당 Raw 데이터를 추출, 가공, 저장

워크플로 관리 : 전체 데이터 파이프라인의 동작 관리

스케쥴링, 모니터링 등등

데이터 레이크 : 데이터를 그대로 축적

모든 데이터를 원래의 형태로 축적해두고 나중에 필요에 따라 가공하는 구조 ~ '데이터 레이크'

임의의 데이터를 저장할 수 있는 분산 스토리지가 사용됨(대부분 csv, json 텍스트 형식을 사용)

데이터 레이크와 데이터 마트 : 필요한 데이터는 마트에 정리

데이터 분석 기반을 단계적으로 발전시키기 : 팀과 역할 분담, 스몰 스타트와 확장

데이터 엔지니어 : 시스템의 구축 및 운용, 자동화(수집-ETL~..)

데이터 분석가 : 데이터에서 가치 있는 정보 추출(..~시각화)

애드 혹 분석 및 대시보드 도구

애드 혹 분석(ad hoc analysis) : 수작업으로 데이터 집계, 일회성 데이터 분석(데이터 레이크, 웨어하우스에 직접 연결하는 경우가 많음)

데이터 마트와 워크플로 관리

복잡한 데이터 분석 전에 데이터 마트 구축을 한다.

(시각화에 BI도구 사용하는 경우 집계 속도를 위해 거의 필수)

데이터 수집 목적 : '검색', '가공', '시각화'

데이터 검색 : 실시간 데이터 처리, 검색 엔진 사용을 통한 키워드 찾는 기능 필요

데이터 가공 : 필요한 데이터를 계획적으로 모아 데이터 파이프라인 설계, 자동화(워크플로)

데이터 시각화 : 소프트웨어, BI 도구를 통해 그래프 생성 + 데이터 마트 구축, 집계 결과를 대시보드에 정리하며 변화 추적

확증적 데이터 분석과 탐색적 데이터 분석

확증적 데이터 분석(confirmatory data analysis) : 가설을 세우고 검증, 통계적

탐색적 데이터 분석(exploratory data analysis) : 데이터를 통해 의미 추출, 시각화

### **[3] BI 도구와 모니터링**

스프레드 시트에 의한 모니터링 : 프로젝트의 현재 상황 파악하기

모니터링 : 계획적으로 데이터의 변화를 추적하는 것

자신의 다음 행동을 결정하기 위한 재료로서 데이터를 관찰함.

데이터에 근거한 의사 결정 : KPI 모니터링

KPI(Key Performance Indicator)

KPI 모니터링에서 의식하고 싶은 것은 그것이 행동 가능(actionable)한 것인지이다.

- > 결과에 따라 자신의 다음 행동이 결정될지의 여부 -> 행동 가능한 숫자를 만들기 위해 그것이 좋은지 나쁜지 판단 기준이 필요함

변화를 파악하고 세부 사항을 이해하기 : BI 도구의 활용

Tableau Public, Quick Sencse, Microsoft Power BI, 구글 Data Studio

데이터의 움직임 모니터링 - 정기적인 변화 파악 - 원인이 되는 데이터에 대해 재집계

수작업 or 자동화

수작업이 가능한 것은 수작업으로

자주 업데이트되거나 다른 사람에게 공유되는 데이터 등 중요성이 높은 것은 자동화 시켜나가기

- BI 도구에서 직접 데이터 소스에 접속하기
- 데이터 마트를 준비하고, 그것을 BI 도구로부터 열기
- 웹 방식의 BI 도구를 도입하여 CSV 파일 업로드하기

도구 선택 시 고려사항

- 저장할 수 있는 데이터 용량에 제한이 없을 것
- 데이터를 효율적으로 추출할 수단이 있을 것

https://velog.io/@kimyj98/%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC-%EC%A7%80%ED%83%B1%ED%95%98%EB%8A%94-%EA%B8%B0%EC%88%A0-ch1

[https://wikidocs.net/185335](https://wikidocs.net/185335)

# DPO

- DPO: direct preference optimization
    - RLHF는 reward 모델이 존재했지만 optimal policy를 계산하는 법을 도출해 reward 모델 없이 simple classification loss 이용해 해결
    - 모델의 확률 값 (log-prob) 활용
    - 얼마나 기존의 reference (base) model 보다 현재의 모델이 confidence 높게 답하는가
- SimPO: simple preference opt.
    - reference 모델에 대한 term이 reward 함수에서 없어지고 평균 로그 확률을 사용
    - 목적 함수에서 reward 에 대한 margin을 둠(gamma) → chosen/rejected 차이 벌리려고
- SIMPER: a minimalist approach  to preference align.
    - 평균 로그확률이 아닌 inverse perplexity(뜻: 예측을 얼마나 잘하는지) 를  적용하여 hyperparameter freeze 한 방법
    - soft reward 적용
        - 기존까지는 classification logit 이어서 선호/비선호 였지만 실제 점수를 예측하게 하자
        - 모델의 확률이 선호 점수의 분포가 되도록 KL divergence 사용
- MDPO: Conditional pref. opt. for mllm
    - DPO 에 visual input 추가해 mm-dpo로 확장
        - 문제는 visual 정보가 힘을 못 씀
        - hard maple 더 넣기 제안 (기존 winning 인 경우 이미지에서 20% 날리고 reject 샘플로 만들기)

### [MPO (**Enhancing the Reasoning Ability of Multimodal Large Language Models via Mixed Preference Optimization)**](https://arxiv.org/abs/2411.10442)

- CoT는 SFT 보다 PO 써야함
    - SFT는 next token prediction으로 답변 생성할때 train 때는 gt, test 할 때는 자기가 생성한 거 바탕으로 next generation 하기에 distribution shift가 존재
    - Multimodal reasoning 향상시킬 데이터셋과 PO 공개
- MMPR dataset
    - general visual question answering (VQA), science, chart, mathematics, OCR, document 데이터로 InternVL로 preference data 생성
    - Multimodal preference data w/ CoT → 3M
    - data contribution pipeline
        - DropoutNTP
            - Clear GT가 없는 question의 경우 InternVL2로 (image, question) 보고 answer 생성
            - negative 생성 시 (~~이미지~~, 질문, a half of answer) 보고 complete answer 해라
                - image 없이 만드니까 hallucination 포함된 negative sample 생성 잘됨
- MPO: mixed preference optimization
    - distribution shift 해결 위해 PO를 MLLM에 통합 (**MLLM의 reasoning 능력을 향상시키기 위해 개발)**
    - **Mixed Loss Function**: MPO는 세 가지 유형의 손실 함수 혼합
        - **선호도 손실(**$L_p$**)**: 응답 쌍 간의 상대적인 선호도를 학습
            - dpo loss 사용
        - **품질 손실(**$L_q$**)**: 개별 응답의 절대적인 품질을 이해하도록 돕습니다. 이 연구에서는 **BCO (Binary Classifier Optimization)** 사용
            - 선택된 응답을 1로, 거부된 응답을 0으로 매핑해 이진 분류기 학습
        - **생성 손실(**$L_g$**)**: 선호하는 응답의 생성 과정을 학습. 이 연구에서는 **지도 학습 기반 미세 조정(SFT) loss** 사용

# Multi-Instruction

- 회사 한 것
    - Multimodal DPO set generation
        - Vision DPO [(image1 image2, q1+q2, a1+a2, a1), (image1 image2, q1+q2, a1+a2, a2)]
        - 한국어 데이터셋 사용 ShareGPT, mantis instruct, aokvqa, clevr
            - ShareGPT
                - Pretrain, 한 비디오에서 10개 유니폼하게 뽑고 gpt4v로 캡션 추출 900k
                - SFT, 비디오 캡션 주고 gpt한테 3개 정도 qa set 만들어 240k, 캡션 재활용 과금 낮춤
                - DPO, gpt(휴먼 대체 평가자) 로 만듬 17k, 텍스트만 넣어서 저렴

### [Multi-Task Inference: Can large language models follow multiple instructions at once?](https://arxiv.org/pdf/2402.11597)

- 다중 작업 추론이 전체 추론 시간을 평균적으로 1.46배 줄일 수 있음
- LLAMA-2-CHAT-70B와 GPT-4 같은 최신 LLMs가 MTI BENCH 다중 작업 추론을 사용할 때 단일 작업 추론보다 각각 최대 7.3% 및 12.4% 향상된 성능

대규모 언어 모델(Large Language Models, LLMs)이 통상적으로 한 번의 추론 호출에 단일 지시사항을 따르도록 요청받는 상황에서, LLMs가 여러 지시사항을 동시에 처리할 수 있는 능력을 분석합니다. 이를 위해, 다중 작업 추론(MULTI-TASK INFERENCE) 능력을 평가하기 위한 종합적인 벤치마크인 MTI BENCH를 소개합니다. MTI BENCH는 25개 작업에서 총 5000개의 인스턴스를 포함하며, 각 작업은 2에서 3개의 하위 작업으로 구성됩니다.
이는 여러 번의 추론 호출이 필요하지 않기 때문입니다. 

![image.png](image%201.png)

최근 배치 프롬프팅(Batch Prompting)과 같은 방법이 제안되어, LLMs가 동일한 작업의 여러 인스턴스를 동시에 처리할 수 있는지를 평가하고 있습니다. 그러나 이러한 방법은 여전히 동일한 작업 내의 인스턴스 처리에 한정되어 있어, 본 논문에서 소개하는 MTI BENCH와 같은, 서로 다른 작업들 사이의 상호작용을 평가하는 데는 제한적입니다.

## Audio modality Continual Learning

- 이미지 데이터셋
    - MSCOCO-2014, and OK-VQA
- 비디오
    - MSVD, MSVD-QA
- 오디오
    - AudioCaps, Clotho-AQA
- point cloud
    - Cap3D, Cap3D-QA