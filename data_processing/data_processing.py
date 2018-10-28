#!/usr/bin/env python 3.6
#-*- coding:utf-8 -*-
# @File    : view_time.py
# @Date    : 2018-10-28
# @Author  : SimonSTYL
# @整理    :黑桃

import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame
from datetime import datetime
import matplotlib.pyplot as plt

"""=====================================================================================================================
1 读取数据
"""
path ="E:/MyPython/SweetOrangeFinance/data_set/"




train_operation = pd.read_csv(path + "train_operation_tag.csv")
test_operation = pd.read_csv(path + "test_operation_tag.csv")

train_transaction=pd.read_csv(path + "train_transaction_tag.csv")
test_transaction=pd.read_csv(path + "test_transaction_tag.csv")

"""=====================================================================================================================
2 数据处理
"""

"""
训练集测试集空缺值分析
"""
temp1=train_transaction.isnull()##将数据中为空的值标记为Ture,不为空的值标记为False


num=(temp1 == True).astype(bool).sum(axis=1)##计算每一行True的总和

is_null=DataFrame(list(zip(num)))## 将num转化为DF

is_null=is_null.rename(columns={0:"is_null_num"})##添加列名


# temp2 = pd.merge(data_transaction,is_null,left_index = True, right_index = True, how = 'outer')
# # temp2 = pd.merge(temp1,is_null,left_index = True, right_index = True, how = 'outer')
#
# temp3=data_transaction.isnull()
#
#
#
# num_column=(temp1 == True).astype(bool).sum(axis=0)
# column_is_null=DataFrame(list(zip(num_column)))
# column_is_null=column_is_null.rename(columns={0:"column_is_null_num"})
# temp2 = temp2.drop(['code1','code2','acc_id2','acc_id3'],axis=1,inplace=True)

train_null = is_null.sort_values(by='is_null_num')
t = train_null.is_null_num.values
x = range(len(t))
plt.scatter(x,t,c='k')
#plt.plot(x,y1,c='b')
plt.title('train set')
plt.xlabel('Order Number(sort increasingly)')
plt.ylabel('Number of Missing Attributes')
plt.ylim(0,25)
plt.show()

data_transaction_test=pd.read_csv(path + "transaction_round1.csv")
temp_test=data_transaction_test
temp_test0=temp_test.isnull()
num=(temp_test0 == True).astype(bool).sum(axis=1)
is_null_test=DataFrame(list(zip(num)))
is_null_test=is_null_test.rename(columns={0:"is_null_num"})
test_null = is_null_test.sort_values(by='is_null_num')
t = test_null.is_null_num.values
x = range(len(t))
plt.scatter(x,t,c='k')
#plt.plot(x,y1,c='b')
plt.title('test set')
plt.xlabel('Order Number(sort increasingly)')
plt.ylabel('Number of Missing Attributes')
plt.ylim(0,25)
plt.show()


"""=====================================================================================================================
缺失值处理
"""
train_transaction['trans_type2']=train_transaction['trans_type2'].fillna(100)##用100 填充trans_type2的缺失值

train_transaction.trans_type2 = train_transaction.trans_type2.apply(lambda x:float(x))

n=set(train_transaction['trans_type1'])
print(n)
n2=list(n)
dic={}
for i,j in enumerate(n):
    dic[j]=i
train_transaction['trans_type1'] = train_transaction['trans_type1'].map(dic)
phone=train_transaction['device_code3']
phone=DataFrame(phone)
phone1=phone.isnull()
phone_size=(phone1 == True).astype(bool).sum(axis=1)
phone2=DataFrame(list(zip(phone_size)))
iphone_android=phone2.rename(columns={0:"phone_size"})



"""


"""
temp=train_transaction
print(temp[0:3])
train_transaction['time'] = pd.to_datetime(train_transaction['time'])
temp.time = temp.time.apply(lambda x:(x-datetime(2018,10,28,0,0,0)).seconds/3600)
temp.time = temp.time.apply(lambda x:int(x))
# print(temp)
temp = temp.sort_values(by='UID')
# temp_right=DataFrame(temp_right)
temp_right= temp[temp.Tag==1]
temp_1 = temp_right[['time','Tag']].groupby('time').agg('sum')
temp_wrong=temp[temp.Tag==0]
temp_wrong['Tag']=1
temp_2 = temp_wrong[['time','Tag']].groupby('time').agg('sum')
temp_1 = temp_1.sort_values(by='time')
temp_2 = temp_2.sort_values(by='time')
ax = temp_1.plot(color='red',title="train set")
temp_2.plot(ax=ax,color='blue')
plt.xlabel('hour')
plt.ylabel('count')
plt.show()



