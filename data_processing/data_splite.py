'''
由于原始数据集太大，读取耗时长，
占用电脑太多内存资源，从原始数据中提取1000条数据
'''
from __future__ import print_function
import sys,csv
import pandas as pd
import time
start_read_time=time.time()
path ="E:/MyPython/SweetOrangeFinance/data_set/"
path_test ="E:/MyPython/SweetOrangeFinance/data_set_test/"
print('————————————————————读取数据———————————————————————————————')

# '''
# 在读取文件的数据时，偶尔会抛出异常：_csv.Error: field larger than field limit (131072)
# 还有一个异常：OverflowError: Python int too large to convert to C long
# 可以看出报错的原因是读取的文件数据太大，加上下面代码后，数据能够正常读取
# '''
#
# maxInt = sys.maxsize
# decrement = True
# while decrement:
#     # decrease the maxInt value by factor 10
#     # as long as the OverflowError occurs.
#     decrement = False
#     try:
#         csv.field_size_limit(maxInt)
#     except OverflowError:
#         maxInt = int(maxInt/10)
#         decrement = True

"""
文件切分
"""
df_operation_TRAIN = pd.read_csv( path + 'operation_TRAIN.csv',nrows=500,engine='python',encoding='gbk')
df_transaction_TRAIN = pd.read_csv(path + 'transaction_TRAIN.csv',nrows=500,engine='python',encoding='gbk')

df_operation_round1 = pd.read_csv(path + 'operation_round1.csv',nrows=500,engine='python',encoding='gbk')
df_transaction_round1 = pd.read_csv(path + 'transaction_round1.csv',nrows=500,engine='python',encoding='gbk')

df_tag_TRAIN = pd.read_csv(path + 'tag_TRAIN.csv',nrows=500,engine='python',encoding='gbk')

# """
# 原始数据的列名可能会出现乱码
# 故改列名
# """
# df_train.columns = ['id','article','word_seg',"class"]
# df_test.columns = ['id','article','word_seg']

"""
保存文件
"""
df_operation_TRAIN.to_csv(path_test + 'operation_TRAIN_test.csv',index=False)
df_transaction_TRAIN.to_csv(path_test + 'transaction_TRAIN_test.csv',index=False)
df_operation_round1.to_csv(path_test + 'operation_round1_test.csv',index=False)
df_transaction_round1.to_csv(path_test + 'transaction_round1_test.csv',index=False)
df_tag_TRAIN.to_csv(path_test + 'tag_TRAIN_test.csv',index=False)



end_read_time=time.time()
print("—————————————读取数据结束，耗时:%.2fs————————————————————————"%(end_read_time-start_read_time))