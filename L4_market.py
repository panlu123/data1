import pandas as pd
import numpy as np


# 数据加载
dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header = None) 
# shape为(7501,20)
print(dataset.shape)

# 将数据存放到transactions中
transactions = []
#按行遍历
for i in range(0, dataset.shape[0]):
    temp = []
    #按列遍历
    for j in range(0, 20):
        #判断不为nan
        if str(dataset.values[i, j]) != 'nan':
           temp.append(str(dataset.values[i, j]))
    transactions.append(temp)
#print(transactions)
# 挖掘频繁项集和频繁规则
from efficient_apriori import apriori

itemsets, rules = apriori(transactions, min_support=0.03,  min_confidence=0.3)
print("频繁项集：", itemsets)
print("关联规则：", rules)
