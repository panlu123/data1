import pandas as pd
import numpy as np

data=pd.read_excel('grade.xlsx')

#语文统计
yuwen_mean=data['语文'].mean()
yuwen_min=data['语文'].min()
yuwen_max=data['语文'].max()
yuwen_var=data['语文'].var()
yuwen_std=data['语文'].std()

#数学统计
shuxue_mean=data['数学'].mean()
shuxue_min=data['数学'].min()
shuxue_max=data['数学'].max()
shuxue_var=data['数学'].var()
shuxue_std=data['数学'].std()

#数学统计
shuxue_mean=data['数学'].mean()
shuxue_min=data['数学'].min()
shuxue_max=data['数学'].max()
shuxue_var=data['数学'].var()
shuxue_std=data['数学'].std()

#英语统计
yingyu_mean=data['英语'].mean()
yingyu_min=data['英语'].min()
yingyu_max=data['英语'].max()
yingyu_var=data['英语'].var()
yingyu_std=data['英语'].std()

#
data['总成绩']=data.loc[0:4,].sum(axis=1)
grade=data.sort_values('总成绩', ascending=False)

