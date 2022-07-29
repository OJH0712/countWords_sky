import jieba
import wordcloud
txt = open("遮天.txt",encoding="utf-8").read()
stopwords = [line.strip() for line in open('停用词库.txt',encoding="utf-8").readlines()]
words = jieba.lcut(txt)
# counts= {}
# for word in words:
#     if word not in stopwords:
#         if len(word) == 1:
#             continue
#         else:
#             counts[word] = counts.get(word,0)+1
# items = list(counts.items())
# items.sort(key = lambda x:x[1],reverse=True)
# for i in range(30):
#     word,count = items[i]
#     print("{:<10}{:>7}".format(word,count))

counts= {}
for word in words:
    if word not in stopwords:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse=True)
sentence = []
for i in range(30):
    word,count = items[i]
    sentence.append(word)
sentence = "".join(sentence)
#这里需要将分好的中文装化成字符串
sentence = " ".join(jieba.lcut(sentence))
print(sentence)
c = wordcloud.WordCloud(width=1000,font_path="msyh.ttc",height=700,background_color="white")
c.generate(sentence)
c.to_file("遮天.png") 