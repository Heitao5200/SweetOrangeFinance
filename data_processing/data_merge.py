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
path_test ="E:/MyPython/SweetOrangeFinance/data_set_test/"
data_operation = pd.read_csv(path + "operation_TRAIN.csv")
data_transaction=pd.read_csv(path + "transaction_TRAIN.csv")
data_tag=pd.read_csv(path + "tag_TRAIN.csv")
data_operation_round1 = pd.read_csv(path + "operation_round1.csv")
data_transaction_round1=pd.read_csv(path + "transaction_round1.csv")
"""=====================================================================================================================
2 数据合并+保存
"""
"""
2.1 训练集数据
"""
## transaction+tag
transaction_tag = pd.merge(data_transaction, data_tag, how='left', left_on='UID',right_on='UID')
transaction_tag.to_csv(path + 'train_transaction_tag.csv',index=False)

## operation+tag
operation_tag = pd.merge(data_operation, data_tag, how='left', left_on='UID',right_on='UID')
operation_tag.to_csv(path + 'train_operation_tag.csv',index=False)

# ## operation+transaction+tag
# operation_transaction_tag = pd.merge(operation_tag, transaction_tag, how='left', left_on='UID',right_on='UID')
# operation_transaction_tag.to_csv(path + 'train_operation_transaction_tag.csv',index=False)
#
# ## 提取operation+transaction+tag数据1000条
# df_train = pd.read_csv( path + 'train_operation_transaction_tag.csv',nrows=1000,engine='python',encoding='gbk')
# df_train.to_csv(path + 'train_set1000.csv',index=False)


"""
2.1 测试集数据operation_round1   transaction_round1
"""

## transaction+tag
data_transaction_round1 = pd.merge(data_transaction_round1, data_tag, how='left', left_on='UID',right_on='UID')
data_transaction_round1.to_csv(path + 'test_transaction_tag.csv',index=False)

## operation+tag
data_operation_round1 = pd.merge(data_operation_round1, data_tag, how='left', left_on='UID',right_on='UID')
data_transaction_round1.to_csv(path + 'test_operation_tag.csv',index=False)