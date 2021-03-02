# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:37:44 2021

@author: Administrator
"""

# 使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np



data = pd.read_csv('car_data.csv', encoding='gbk')
print(data)
train_x=data[['人均GDP','城镇人口比重','交通工具消费价格指数','百户拥有汽车量']]


#归一化
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
pd.DataFrame(train_x).to_csv('temp.csv', index=False)
print(train_x)

### 使用KMeans聚类
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)

#合并结果
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)

