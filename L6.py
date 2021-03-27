import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

#导入数据
train = pd.read_csv('./train.csv')
#转化为时间类型
train['Datetime']=pd.to_datetime(train['Datetime'])


#datetime作为index
train.index=train['Datetime']

#删掉不必要的列
train.drop(['ID','Datetime'],axis=1,inplace=True)

#按天采样
daily_train=train.resample('D').sum()



daily_train['ds']=daily_train.index
daily_train['y']=daily_train['Count']
daily_train.drop(['Count'],axis=1,inplace=True)

#创建模型
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
#训练
m.fit(daily_train)
#预测
future = m.make_future_dataframe(periods=213)
forecast=m.predict(future)

m.plot(forecast)