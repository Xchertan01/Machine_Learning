# -*- coding = utf-8 -*-
# @Software: Pycharm

import numpy as np
import pandas as pd
from collections import Counter
from functools import reduce
import matplotlib.pyplot as plt
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决Matplotlib坐标轴负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

plt.style.use('ggplot')

bank_train = pd.read_csv("D:\Python\Machine_Learning\数据\modeldata\bank_train.csv")
salary_df = bank_train[bank_train["工资收入标记"] == 1].groupby("new_user_id")["交易金额"].agg("mean").reset_index()
_df = bank_train[bank_train["工资收入标记"] == 0].groupby("new_user_id")["交易金额"].agg("mean").reset_index()
salary_df = pd.merge(salary_df, _df, on='new_user_id', how='left')
salary_df.columns = ['new_user_id', '平均工资收入', '非工资平均收入']
x, y = salary_df['平均工资收入'], salary_df['非工资平均收入']
m = len(x)

