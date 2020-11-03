## 基于one-hot文本表示

### words representation

#### one-hot
词典 = ['你','大家好','早上好','希望','非常','开心']

非常 = [0,0,0,0,1,0]

大家好 = [0,1,0,0,0,0]


### sentence representation
词典 = ['你','大家好','早上好','希望','非常','开心']
#### Boolean representation

你 非常 开心 = [1,0,0,0,1,1]
你 希望 你 开心 = [1,0,0,1,0,1]


#### count based representation
你 非常 开心 = [1,0,0,0,1,1]
你 希望 你 开心 = [2,0,0,1,0,1]


#### tf-idf representation

tfidf(w) = tf(d,w)*idf(w)

##### 1、tf(d,w)
>文档d中w的词频

##### 2、idf(w)
>考虑单词的重要性

>log(N/N(w))

- N:语料库中的文档总数
- N(w):词语w出现在多少个文档

##### 3、例子：
![image](https://github.com/ash-ali/nlp-learn/blob/master/img/tdidf.png)


##### 4、td-idf应用
>权重计算方法经常会和余弦相似度(cosine similarity)一同使用于向量空间模型中，用以判断两份文件之间的相似性

##### 5、tf-idf存在的意义
基于count based的文本向量表示，会出现一个问题就是：某个单词出现越多就一定越重要。而有时候却不是如此，tf-idf就是为了解决：

- 并不是出现的越多就越重要
- 并不是出现的越少就越不重要

关于tf-idf还可以参考
- https://baike.baidu.com/item/tf-idf/8816134?fr=aladdin
- https://zhuanlan.zhihu.com/p/113017752
 

