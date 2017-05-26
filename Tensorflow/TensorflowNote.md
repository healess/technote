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
