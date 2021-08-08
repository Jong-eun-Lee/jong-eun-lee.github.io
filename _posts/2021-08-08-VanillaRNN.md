---
layout: post
title: Vanilla RNN (updating)
date: 2021-08-08 14:59:31 +0900
category: NLP
---
## Vanilla RNN
RNN은 sequential data를 처리하기에 적합한 모델이다.  
과거의 정보를 현재에 반영하여 학습하도록 설계됐고,  
hidden state 값은 현재의 input과 이전 hidden state의 영향을 받는다.<br><br>
![POStagging](https://user-images.githubusercontent.com/67620728/128625984-46c16abe-c87d-4f5f-a7c6-72061643c311.PNG)<br>
위 자료는 POS Tagging을 위한 RNN 구조이고,
![sentimentAnalysis](https://user-images.githubusercontent.com/67620728/128626131-fa1ccb38-7ecd-4cc4-85ec-18f80852f307.PNG)<br>
위 자료는 Sentiment Analysis를 위한 RNN 구조이다.<br><br>
학습 방법으로는 Backpropagation Through Time(BPTT)을 채택하는데,  
자료에서 여러 번 등장하는 Wxh 등은 등장할 때마다 다른 변수인 것이 아니라  
동일한 변수다. 고로 각 time series마다 동일한 변수를 바꾸는 것이기 때문에
Backpropagation Algorithm이 아닌 BPTT를 채택하는 것이다.<br><br>
### RNN의 문제점
1. Parallel computing을 구현하기 어렵다.
2. Long sequences를 다룰 경우 정보의 손실이 있을 수 있다.
3. Vanishing gradient 문제가 있다.
