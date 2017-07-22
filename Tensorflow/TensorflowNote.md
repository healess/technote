# Reference URL
- ![남중구선생님](http://dlwiki.finfra.com/start)
- ![북마크](https://github.com/hyunjun/bookmarks/blob/master/nlp.md)

## Tensorflow
### RNN 
 - vocab_size = 8000 #높은단어 순 8000개
 - batch_size = 4 # 문답문답 2쌍 4개
 - checkpoint_step = 100 #모델의 100단계별 저장 및 출력
 - buckets = [(8, 15)] # 입력길이에 따른 출력 값 길이 


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
- Back Propagation : 모델 학습( Train )
- forward Propagation : 모델 적용 ( Test, Implemetation )
- Iteration : 학습의 한 단계(Epoch)
- Training/Test : 학습/검증
- Overfitting : 과도학습
- Test Error : (Overfitting이 많이 된 상태)
- Regularization : Test Error를 줄이기 위해 결과를 일반화(Overfitting 방지)
- Dropout : 임의로 perceptron 일부를 작동 안시키시고 학습
- soft-max : 합계가 1이되는 확률값의 집합
- one-hot encoding : 3→ 0,0,0,1,0,0,0,0,0,0,  2→0,0,1,0,0,0,0,0,
- Semi-supervised Learning : Supervised Learning 준비하고, Unsupervised Learning으로 분석, 그 반대도.
- Representation Learning : Unsupervised Learning

## Chatbot (패스트캠퍼스강의정리)
##from company.ai (챗봇,자연어 처리 전문 Startup)
### NER(Named-Entity Recognition)
 - NER:Frame Based DM) - 최근에 Seq2Seq모델 사용 (미비한 부분은 Rule로 보완)
 - JSON형태로 템플릿을 구성해서 NER을 뽑아냄
 (ex.회의실예약의 경우 (필수 파라미터 구성) -> 명사만 뽑아냄 (company.ai의 경우 Crawling를 통한 자체 Corpus구축/POS포함)
 - New York -> NewYork 의 구분 필요 (Tagging - New York(B-Origin) -> NewYork(I-Origin))
 - NER이 핵심(Seq2Seq를 활용 Decoder에 POS, entity 등등 한번에 처리 - 자체 Corpus 및 분석기 활용 - 오늘 날씨가 머지? >> day weather intent verb)
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
 - 틀리면 아예 SLot를 봇에 보여주는 방법도 많이쓰임(사이즈,수량) - NER 파악 하기 힘들경우 (SLOT는 하드코딩도 가능)
 - 커스텀 값인식에는 CNN이 유용 (전화번호 패턴, 특수명사등)

### Pointer Network
 - Decoder의 길이가 다를 경우 Seq2Seq로는 한계 (용도: 물류 문제 해결) -> 독해문제 (Machine Comprehension) -> 문맥의 특정 단어의 조합을 연결)
 - 해당 문맥을 통해 특정 Pointer들을 찾음 (집으로 가는 가장 빠른 길을 찾아줘)

### GAN vs VAE
#### GAN
 - NLP쪽은 아직까지 사용한 사례 없음 (굉장히 많은 Data 가 있어야함) 
 - 판별하는 모델을 사용해서 GAN으로 효과를 봄 (평가단계에서는 활용해서 활용 - 튜링테스트)
 - 주로 이미지에서 사용 (선명한 이미지 VAE보다 나음)
 - 괜찮은 자료 !Pycon2016 지적 대화를 위한 깊고 넓은 딥러닝 (Feat. TensorFlow)[https://www.pycon.kr/2016apac/program/9]
### VAE
 - VAE : 확률 기반 모델,  빠르고 에러가 적은편, input data가 실수가 아니더라도 이미지, 텍스트등 가능
 - VAE는 자연언어처리의 핵심 (Predict보다 Count쪽에 가까움)

## Optimizer
 - Convex의 정의를 알고 이해하면 쉬움
 - GD vs SGD : GD는 한방향으로 가는데 반해 SGD (Stochestic) 보이는 곳을 따라감 Optimal하지는 않음 충분한 시간이 지나면 찾음
 - 수학적으로 GD는 Iter의 횟수에 따라 무조건 작아짐
 - Optimizer 팁 : Loss값에 따른 Learning 를 내림(순수 Adam과는 다른 코드상의 처리) ex) Loss값이 2번연속 증가하면 Learning Rate 1%줄이는 방법
 - Object function에따라 Loss Function이다름 (Cifar 10의 경우 Adam이 답이 아님 -> Adaptive optimization가 최근 더 효과를 봄 5/23 논문)
 - Deep Learning에서 Optimizer이 전체에서 50%이상의 비중을 차지함 (SGD? Adam?) 나머지는 데이터 정제 50%

### 기타
 - Torch 강점 : 빠른 Prototype, 쉬운 문법, Lua와 속도는 같음
 - 챗봇은 UI/UX관점에서 질문은 짧더라도 답변은 길고 계속 이어갈 수 있게 가는게 좋음
 - 넷플릭스 경진대회 에피소드 10억을 받기위해 90%의 정확도를 참가자들의 89% 모델의 앙상블로 해결해서 상금 나눔
 - 챗봇 결국은 서비스 관점에서 검색도 잘해야함
 - Embedding보다는 (원본을 가져가서 one hot으로 쓰는 경우가 많음)
 - Maxpool은 결국 엠프 역활이라보면됨
 - RBM : 실수가 나오면서 큰 의미가없음 (2000후반이후) Softmax와 유사 (RBM은 추가 파라미터)
 - 자연어는 컴퓨팅 파워에 영향이 적음(이미지처럼 병렬처리가아닌 aggregation의 특성상 : 문장은 완성되야 의미가 나옴)
 - 최근에 Facebook에서 밀고 있는 이미지 -> 설명하는 것(엉어로 잘됨 : 페이스북) : 이미지 to vector 기술
 - seq2seq모델은 레이어를 최소화해야함
 - Chatbot에서 Data의 의미는 실재 성별은 무시해야함 ex. 우리가 작성한 성별은 버려라(넥플릭스 - 여성향인 남자도 있기에..)
 - 2014년 이후 번역은 SMT -> NMT로 seq2seq모델을 통해 문맥을 이해함으로써 정확도가 올라감 (ETRI 지니톡 도 같은 예기했었음)
 - 모델이 복잡할 수록 마지막 레이어에 원본을 넣는게 좋다 (Gating Network highway)
 ![참조](https://www.researchgate.net/profile/Hussein_Dia/publication/43462129/figure/fig2/AS:289373795962881@1446003497132/Figure-2-Proposed-Neural-Network-Architecture.png)
 - 1달안에 챗봇개발?? : 목표가 명확하면 빨리 실력이 늘고 업그레이드됨 - 일반 학계는 회사 실무보다 늦음

#### Ranking 
 - Pointwise (여러 리스트 중에 최적값을 도출) 너무 작은 값에서는 잘 찾지 못함) 0.11과 0.12 : IE: {d1, r1} {d2, r2} {d3, r3} {d4, r4}
 - Pairwise (하나씩 비교) 0 또는 1 => 더 효과를 봄 : IE: {d1 > d2} {d2 > d3} {d3 > d4}
 
## Text Classification
[참조](https://www.slideshare.net/ssusere94328/deep-learning-text-nlp-and-spark-collaboration-text-nlp-spark)
 - mecab 처럼 형태소를 잘게 쪼개는 것보다, twitter.pos 에 stem 옵션 주고 될수 있는한 동사등도 원형을 써서 generalization화 해주는게 data 가 작은 경우 성능 향상에 도움이 됨. 조사나 특수기호등은 당연히 제가(데이타가 작을때)
 - Tensorflow CNN word2vec 기반 (Data가 많을때 성능이 좋음)
 - Scikit-learn SVM (linear-kernel) 기반
 - Scikit-learn SVM (rbf-kernel) 기반
 - Scikit-learn MultinomialNB TF-IDF 기반
 -  naive bayse, SVM, Random Forest