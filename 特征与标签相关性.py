# -*- coding = utf-8 -*-
# @Software: Pycharm

 # 绘制简单热力图，来表示相关性。本代码不完全，待补充。

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决Matplotlib坐标轴负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

userinfo = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\userinfo_train.csv")
overdue = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\overdue_train.csv")

userinfo_merge = pd.merge(userinfo, overdue, on='new_user_id')
def corr(Data):
    sns.set(font='SimHei')
    plt.rcParams['axes.unicode_minus']=False
    corr = Data.corr()
    plt.subplots(figsize=(15,12))
    sns.heatmap(corr, vmax=0.9, cmap="YlGnBu", square=True)
    plt.show()

corr(userinfo_merge.drop(['new_user_id'], axis=1))
