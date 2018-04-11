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
import pymysql as sql

# hyperparameter
itemId_list = ['549049522944', '552919553653']  # '560597539512', 
sellerId_list = ['1714128138', '1114511827']  #'2616970884',
name_list = ['xiaomi_6', 'huawei_rongyao_9']  #'iphone_X', 

# comments_num 4.8w 12.6w 17.5w

# connect mysql
con = sql.connect(host='localhost', user='root',passwd='',db='taobao',charset='utf8')

# begin
for itemId, sellerId, name in zip(itemId_list, sellerId_list, name_list):
    total_pages = 6000
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
    # mysql
    for i in range(len(comments)):
        cursor = con.cursor()
        query = ('insert into ' + name + '(comments) values (%s)')
        cursor.execute(query, (comments[i]))
        con.commit()
        cursor.close()
    con.close()
     
    # csv
    tb = codecs.open('tb_' + name + '_comments.csv', 'w', 'utf_8_sig')
    writer = csv.writer(tb)
    for i in range(len(comments)):
        writer.writerow([comments[i]])
    tb.close()
    end = time.time()
    print('{0} ---- Total {1:.3f} s !'.format(name, end-begin))





















