## language model

### 1、对于一个好的language model
p(he is studying AI) > p(he studying AI is)

### 2、如何计算p
- 【uni-gram】p(he is studying AI) = p(he)p(is)p(studying)p(AI)
- 【Bi-gram】p(he is studying AI) = p(he)p(is|he)p(studying|is)p(AI|studying)
- ...

条件概率p(is|he):以he作为is出来之前的条件，概率是多少

### 3、uni-gram、Bi-gram、Tri-gram(markov Assumption)
![image](https://github.com/ash-ali/nlp-learn/blob/master/img/joint_probability.png)
p(X1,X2,X3,X4)为联合概率(joint probability)

p(X1,X2,X3,X4) = p(X1)p(X2|X1)p(X3|X1X2)p(X4|X1X2X3) 

#### uni-gram
>由于计算条件概率的复杂性，uni-gram不考虑条件概率，看作独立事件（假设）

uni-gram = p(X1)p(X2)p(X3)p(X4)

#### Bi-gram
>考虑前一项的条件概率

Bi-gram = p(X1)p(X2|X1)p(X3|X2)p(X4|X3)


#### Tri-gram
>考虑前两项的条件概率

Tri-gram = p(X1)p(X2|X1)p(X3|X1X2)p(X4|X2X3)
