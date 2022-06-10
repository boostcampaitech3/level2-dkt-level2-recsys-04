# RecSys 04 - 마음에들조
---

# DKT : Deep Knowledge Tracing

## 대회 소개 및 개요

DKT는 Deep Knowledge Tracing의 약자로 우리의 "지식 상태"를 추적하는 딥러닝 방법론입니다.  
DKT를 활용하면 학생 개개인에게 수학의 이해도와 취약한 부분을 극복하기 위해 어떤 문제들을 풀면 좋을지 추천이 가능합니다. DKT는 맞춤화된 교육을 제공하기 위해 아주 중요한 역할을 맡게 됩니다.  
대회에서는 Iscream 데이터셋을 활용합니다. 주어진 문제를 맞출지 틀릴지 예측하는 것에 집중할 것입니다. 각 학생이 푼 문제 리스트와 정답 여부가 담긴 데이터를 받아 최종 문제를 맞출지 틀릴지 예측합니다.

## 데이터

- Input : 약 7000명의 사용자들의 문제 풀이 내역
- Output : 사용자들의 마지막 문제 정답여부 (-1 로 표시된 문제들)
  
## 모델

- 시도한 모델
  - ML
    - Linear Regression
    - Logistic Regression
    - XGBoost
    - CatBoost
    - LGBM
  - DL
    - LSTM
    - BERT
  - LGBM, CatBoost 7:3 소프트보팅
  - LGBM + CatBoost Ensemble (7:3 Weighted Soft Voting)

## 결과

- Public LB AUROC : 0.8319 (Top 2)
- Private LB AUROC : 0.8401 (Top 10)

