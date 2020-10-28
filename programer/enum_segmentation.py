#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : linjie
# 基于枚举的分词

import pandas as pd
import math
path = r'/Users/linjie/资料_1/Project1-master-6969c54c279dbdb8196c1ae07e1b4a60b9c49436/data/综合类中文词库.xlsx'


'''
思路：
1、读取词库
2、为词库进行概率设置
3、对原始文本进行分词，获得所有分词结果
4、根据分词结果得到概率最大的结果
'''

'''
step1：读取语料库
'''
dic = pd.read_excel(path,header=None)
dic_words = set(dic[0].tolist())    # 保存词典库中读取的单词



'''
step2：为语料库的词进行概率设置（这里只模拟了部分词的概率）  
'''
word_prob = {"做作":0.78,"做针线":0.08,"做戏":0.005,"做文章":0.005,"你":0.06,"真":0.003,"做":0.04,"作":0.03}
print(sum(word_prob.values()))


'''
step3：对获取的文本进行分词，这里使用里递归的分词方法
instance：str = "北京"   --->   result：list = [['北', '京'], ['北京']]
'''
# 利用递归计算所有可行的分词之后的结果
def word_break(s, dic):
    '''
    分词
    :param s: 原始文本
    :param dic: 词典库中读取的所有词
    :return: list型的分词结果
    '''
    def sentences(cur):
        result=[]
        if cur <len(s):
            for next in range(cur+1, len(s)+1):
                if s[cur:next] in dic:
                    result = result+[s[cur:next]+(tail and','+tail) for tail in sentences(next)]#因为递归所有cur会加1
        else:
            return ['']
        return result

    list_new = []
    for line in sentences(0):
        line = line.split(",")
        list_new.append(line)
    return list_new


'''
step4:根据分词结果得到概率最大的结果
'''
def get_probability_reult(input_str):
    '''
    概率比较
    :param input_str: 原始文本
    :return: 概率
    '''
    segments = word_break(input_str,  dic_words)  # 存储所有分词的结果
    print(f'基于word_prob的所有的分词结果：{segments}')

    #循环所有的分词结果，并计算出概率，概率高的即为分词结果
    best_segment = []
    best_score = -math.inf  # best_score初始值等于负无穷小
    for seg in segments:
        score = 0
        for w in seg:
            if w in word_prob.keys():
                score += word_prob[w]
            else:
                score += 0.000001
        if score > best_score:
            best_score = score
            best_segment = seg
            print(f'分词结果：{best_segment},得分：{best_score}')
    return best_segment


if __name__ == '__main__':
    print(get_probability_reult("你真做作"))