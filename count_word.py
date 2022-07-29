from ast import NotIn
from itertools import count
import jieba
from pyparsing import WordStart
txt = open("遮天.txt",encoding="utf-8").read()
stopwords = [line.strip() for line in open('停用词库.txt',encoding="utf-8").readlines()]
words = jieba.lcut(txt)
counts= {}
for word in words:
    if word not in stopwords:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse=True)
for i in range(30):
    word,count = items[i]
    print("{:<10}{:>7}".format(word,count))