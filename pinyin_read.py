from pypinyin import pinyin, lazy_pinyin, Style
import numpy as np


f = open(r'C:\Users\86183\Desktop\aaa.txt')
Chinese_file = f.read()
pinyin = pinyin(Chinese_file)

pinyin_file = []
for i in np.arange(len(pinyin)):
    pinyin_file = pinyin_file + pinyin[i]
print(pinyin_file)
f.close()


# pinyin_name = pinyin('首孝弟  次见闻    知某数  识某文  一而十  十而百  百而千  千而万 路过 不巧 便条 派对 计划 邀请 抱歉 没法儿 正好 肯定 不许 前一天 惊喜 快乐')
# print(pinyin_name)
