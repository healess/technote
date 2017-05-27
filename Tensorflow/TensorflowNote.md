# Reference URL
http://dlwiki.finfra.com/start

# Deep Learning 용어
Perceptron
weight
Learning Rate(c)
Error Function
Optimizer   
Activation Function
Bias
Iteration(Epoch)
Back Propagation : 모델 학습( Train )
Forward Propagation : 모델 적용 ( Test, Implemetation )
Regularization : Overfitting을 방지

## GPU
|name    |core count |1000won|
|--------|-----------|--------|
|Titan-X |3072       |150     |
|980ti   |2600       |95      |
|1080    |2400       |90      |
|1060    |1260       |37      |
* 1080부터는 power에 신경쓰셔야 됨.

## Deep Learning 용어
- Perceptron : 뇌세포를 구현
- Weight : 기억
- Learning Rate : 학습률
- Activation Function : ex) Sigmoid, ReLu
- Loss Function : 실제값-결과값
- Layer : MLP에서 Perceptron을 쌓은 단
- 학습이 일어난다 : Error Function을 미분해서 Learning Rate곱해서 에러가 최소화되는 Weight을 찾음.
- Back Propagation : 학습(여러층)
- forward Propagation : 적용(여러층)
- Iteration : 학습의 한 단계
- Training/Test : 학습/검증
- Overfitting : 과도학습
- Test Error : (Overfitting이 많이 된 상태)
- Regularization : Test Error를 줄이기 위해 결과를 일반화
- Dropout : 임의로 perceptron 일부를 작동 안시키시고 학습
- soft-max : 합계가 1이되는 확률값의 집합
- one-hot encoding : 3→ 0,0,0,1,0,0,0,0,0,0,  2→0,0,1,0,0,0,0,0,
- Semi-supervised Learning : Supervised Learning 준비하고, Unsupervised Learning으로 분석, 그 반대도.
- Representation Learning : Unsupervised Learning

## Chatbot (패스트캠퍼스강의정리)

## from company.ai (챗봇,자연어 처리 전문 Startup)

### NER(Named-Entity Recognition)
 - NER:Frame Based DM) - 최근에 Seq2Seq모델 사용 (미비한 부분은 Rule로 보완)
 - JSON형태로 템플릿을 구성해서 NER을 뽑아냄
 (ex.회의실예약의 경우 (필수 파라미터 구성) -> 명사만 뽑아냄 (company.ai의 경우 Crawling를 통한 자체 Corpus구축/POS포함)
 - New York -> NewYork 의 구분 필요 (Tagging - New York(B-Origin) -> NewYork(I-Origin))
 - NER이 핵심
 - 네이버의 챗봇 주문 역시 (틀 안에서 선택할 수 있게함) - Slot을 채우는 형태 (final state)
 - 제외하고등에 대한 Slot 구성은 분리 (한번 선택해서 가게함)
 - 유연하게 왔다갔다하게 하면서 frame의 구성NER의 구성(동일 도메인 내에서 처리) 
 - Attention Newtork -> Seq2seq모델의 길이가 길어질수록 떨어지는 문제(Seq의 Encoder이 길이는 다른데 백터 값은 같음) 해결
 - encoder의 누적값으로 해결
 - 번역에도 유용하나 챗봇의 필요한 요소들을 해결 (NER의 정보)
 - soft attention(평균값) / max attention(MAX값찾음)
 - 고유명사는 하드코딩해야함
 - Syntaxnet(구문분석) : 챗봇이 고도화되었을때 주로 사용
 - 한글은 자소관리로 분해(unicode로 초성,중성,종성) 
 - 개인정보보호 (식별부분도 고려되야함)

### Pointer Network
 - Decoder의 길이가 다를 경우 Seq2Seq로는 한계 (용도: 물류 문제 해결) -> 독해문제 (Machine Comprehension) -> 문맥의 특정 단어의 조합을 연결)
 - 해당 문맥을 통해 특정 Pointer들을 찾음 (집으로 가는 가장 빠른 길을 찾아줘)

### 기타
 - Torch 강점 : 빠른 Prototype, 쉬운 문법, Lua와 속도는 같음
 - 챗봇은 UI/UX관점에서 질문은 짧더라도 답변은 길고 계속 이어갈 수 있게 가는게 좋음
 - Optimizer 팁 : Loss값에 따른 Learning 를 내림(순수 Adam과는 다른 코드상의 처리) ex) Loss값이 2번연속 증가하면 Learning Rate 1%줄이는 방법
 - Object function에따라 Loss Function이다름 (Cifar 10의 경우 Adam이 답이 아님)
 - GD vs SGD : GD는 한방향으로 가는데 반해 SGD (Stochestic) 보이는 곳을 따라감 Optimal하지는 않음 충분한 시간이 지나면 찾음
 - 수학적으로 GD는 Iter의 횟수에 따라 무조건 작아짐
 - Deep Learning에서 Optimizer이 전체에서 50%이상의 비중을 차지함 (SGD? Adam?) 나머지는 데이터 정제 50%
 - 넷플릭스 경진대회 에피소드 10억을 받기위해 90%의 정확도를 참가자들의 89% 모델의 앙상블로 해결해서 상금 나눔
 - 챗봇 결국은 서비스 관점에서 검색도 잘해야함
 - Embedding보다는 (원본을 가져가서 one hot으로 쓰는 경우가 많음)
 - Maxpool은 결국 엠프 역활이라보면됨
