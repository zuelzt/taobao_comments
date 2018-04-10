#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:51:42 2018

@author: Rorschach
@mail: 188581221@qq.com
"""
import warnings
warnings.filterwarnings('ignore')

import requests as rq
import re
import csv
import codecs

total_pages = 200
comments = []
for i in range(100):
    page = str(i+1)
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=560597539512&sellerId=2616970884&currentPage=' + page
    myweb = rq.get(url)
    co = re.findall('\"rateContent\":(\".*?\")\,\"rateDate\"', myweb.text)
    for num in range(len(co)):
        comments.append(co[num][1:-1])

tb = codecs.open('tb_iphoneX_comments.csv', 'w', 'utf_8_sig')
writer = csv.writer(tb)
for i in range(len(comments)):
    writer.writerow([comments[i]])
tb.close()
    





















