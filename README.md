# 2022 인공지능 기초 Repository @*Sangmyung Univ.*  
   > ### Course for Basic Artificial Intelligence in 2022  
   >   >_TextBook_: [*밑바닥부터 시작하는 딥러닝 1*](https://www.hanbit.co.kr/store/books/look.php?p_code=B8475831198)

## Dir Info.  
|Name|Description|Tag|  
|:---:|:---:|:---:|    
|Beginner_300|파이썬 초보자를 위한 300제|[파이썬 300제](https://wikidocs.net/book/922)|  
|Intermediate_100|파이썬 중급자를 위한 100제|[파이썬 100제](https://www.notion.so/Python-100-6ee1860ce29a41bc8eb6b9cfa7d7f06c)|  
|Week 01 ~ 15|수업시간 코드 업로드|-|

# Regression과 Classification  
   > Regression (회귀)     : 입력변수에 대하여 연속적인 값을 도출하는 모델  
   > Classification(분류)  : 입력변수에 대하여 이산적인 값을 도출하는 모델  

   >Example)  
   > 다음주 서울의 기압(kPa) 예측               --> 회귀  
   > 다음주 서울의 날씨(좋음, 나쁨, 흐림) 예측  --> 분류  

# Regression의 종류  
   > y = Wx + B  
   > Sigmoid(x) = 1 / (1 + exp(-x))  
   > Softmax(x) = exp(x) / sum(exp(x(i)))  
   > (W: Weight, B: Bias)  


   |Class|No. Of Answer|Hypothesis Function|Tag|  
   |:---:|:---:|:---:|:---:|  
   |Linear Regression| - | y(=Wx + B) | - |  
   |Logistic Regression| 2 | Sigmoid(y) | - |  
   |Multinominal Regression| Above 3 | Softmax(y) | - |  

#### (This Repository is forked from __*idsdlab/basicai_fa22*__)  
