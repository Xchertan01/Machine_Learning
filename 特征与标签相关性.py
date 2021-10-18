# -*- coding = utf-8 -*-
# @Software: Pycharm


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决Matplotlib坐标轴负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

userinfo = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\userinfo_train.csv")
overdue = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\overdue_train.csv")