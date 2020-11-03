#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : linjie
# tfidf文本表示
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()#实例化tdidf
'''
原始文档
'''
text = [
    'one two document blue'
    ,'two two document'
]
#训练，构建词汇表以及tdidf值
vec_fit = vectorizer.fit_transform(text)
print(vectorizer.get_feature_names())
#['blue', 'document', 'one', 'two']

#打印平滑tdidf矩阵
vec_fit.toarray()
#array([[0.57615236, 0.40993715, 0.57615236, 0.40993715],
#       [0.        , 0.4472136 , 0.        , 0.89442719]])

'''
测试文档
'''
test_text = ['one document yellow']
test_vec_fit = vectorizer.transform(test_text)
print(vectorizer.get_feature_names())
#['blue', 'document', 'one', 'two']
test_vec_fit.toarray()
#array([[0.        , 0.57973867, 0.81480247, 0.        ]])