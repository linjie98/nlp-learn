## Distributed representation

### 1、优势

- 长度不依赖于词典（解决Sparsity问题）
- 向量里面每个位置基本都有数值（非0值）


### 2、针对单词的Distributed representation————词向量
> 词向量是是Distributed representation中的一种 

> 在理想情况下，词向量在某种意义上，理解成词的意思(meaning)







### 3、Comparing the capacities

> 100维的one-hot representation 最多可以表示多少个不同的单词？

向量的大小 = 100，例如：我们:(1,0,0,0,...0),运动:(0,1,0,0,...0)

所以可以表示10个不同单词

> 100维的Distributed representation 最多可以表示多少个不同的单词？

1、例如：我们:(0.1,0.2,0.5......)

所以理论上是无穷个


2、假设我们限制数值只能是0和1，我们:(1,0,0,1,1,0.....)，每个位置上是0/1

所以有2^100个不同的单词

### 4、From word Embedding to sentence Embedding

- 法1：averaging法则
- 法2：LSTM/RNN