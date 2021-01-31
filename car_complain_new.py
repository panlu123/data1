


# 对汽车投诉信息进行分析
import pandas as pd

result = pd.read_csv('car_complain.csv')
#print(result)
# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
print(result.columns)
tags = result.columns[7:]
#print(tags)


df= result.groupby(['brand'])['id'].agg(['count'])
df2= result.groupby(['brand'])[tags].agg(['sum'])
df2 = df.merge(df2, left_index=True, right_index=True, how='left')
# 通过reset_index将DataFrameGroupBy => DataFrame
df2.reset_index(inplace=True)
df2= df2.sort_values('count', ascending=False)

#品牌投诉数
print(df2)

#车型投诉数
df0=result.groupby(['car_model'])['id'].agg(['count'])
df3= result.groupby(['car_model'])[tags].agg(['sum'])
df3 = df0.merge(df3, left_index=True, right_index=True, how='left')
# 通过reset_index将DataFrameGroupBy => DataFrame
df3.reset_index(inplace=True)
df3= df3.sort_values('count', ascending=False)

#平均车型投诉数
data=result.groupby(['brand','car_model'])['car_model'].agg(['count'])
data.reset_index(inplace=True)

model=data.groupby(['brand'])['car_model'].nunique()
model=pd.DataFrame(model)
average=df['count']/model['car_model']

average= average.sort_values( ascending=False)
