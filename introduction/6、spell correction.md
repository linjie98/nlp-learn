## spell correction

#### 1、流程
![image](https://github.com/ash-ali/nlp-learn/blob/master/img/spell_correction.png)


#### 2、how to filter?
>输入字符串s，我们要找出最有可能成为正确的字符串c，也就是如下公式

![image](https://github.com/ash-ali/nlp-learn/blob/master/img/c_candidates.png)

>candidates是已知的候选集合，公式含义：找到c使得p(c|s)最大，并返回c的值(c hat)


##### 计算此公式

![image](https://github.com/ash-ali/nlp-learn/blob/master/img/c_argmax.png)

