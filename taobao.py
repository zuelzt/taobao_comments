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
import time

# hyperparameter
itemId_list = ['560597539512', '549049522944', '552919553653']
sellerId_list = ['2616970884', '1714128138', '1114511827']
name_list = ['iphone_X', 'xiaomi_6', 'huawei_rongyao_9']

# comments_num 4.8w 12.6w 17.5w

# begin
for itemId, sellerId, name in zip(itemId_list, sellerId_list, name_list):
    total_pages = 500
    count = 0
    comments = []
    begin = time.time()
    for i in range(total_pages):
        page = str(i+1)
        url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=' + itemId +'&sellerId=' + sellerId + '&currentPage=' + page
        myweb = rq.get(url)
        co = re.findall('\"rateContent\":(\".*?\")\,\"rateDate\"', myweb.text)
        for num in range(len(co)):
            comments.append(co[num][1:-1])
            count += 1
            print('get No. {}'.format(count))

    tb = codecs.open('tb_' + name + '_comments.csv', 'w', 'utf_8_sig')
    writer = csv.writer(tb)
    for i in range(len(comments)):
        writer.writerow([comments[i]])
    tb.close()
    end = time.time()
    print('{0} ---- Total {1:.3f} s !'.format(name, end-begin))
