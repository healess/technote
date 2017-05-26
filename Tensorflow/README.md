# 초간단 챗봇 구현 소스

#### [Reference Code]: https://github.com/golbin/TensorFlow-Tutorials/blob/master/08%20-%20RNN/03%20-%20Seq2Seq.py
#### 추가 구현 기능 내역
1. 기존 Seq2Seq를 활용한 번역 방식을 챗봇형태의 방식으로 변경 
2. plot를 활용하여 Train확인을 위한 시각화 추가
3. Response 함수 추가를 통해 답변 다양화
4. 버젼 Migration을 통한 오류 해결
5. Model저장 (./model)


#### Migration
- TF v1.1 / Python 3.5 / Solve Variable Scope Error (Initalize Graph)

#### Result
- 나 : 안녕
- 봇 : 반가워 봇
<br><br>
- 나 : 머해
- 봇 : Tensorflow 수업듣고 있어
<br><br>
- 나 : 누가
- 봇 : 남중구 선생님한테 배우고 있어
<br><br>
- 나 : 예뻐
- 봇 : 남자 선생님이야;;
<br><br>
- 나 : 어때
- 봇 : 잘가르쳐 주시고 많이 배우고 있어
<br><br>
- 나 : 바보
- 봇 : 남자 선생님이야;;
<br><br>
- 나 : 그래
- 봇 : 그래 안녕~
