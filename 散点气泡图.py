# -*- coding = utf-8 -*-
# @Software: Pycharm

#  散点图
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决Matplotlib坐标轴负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

userinfo = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\userinfo_train.csv")
overdue = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\overdue_train.csv")
userinfo.columns = ["new_user_id", "性别", "职业", "教育程度", "婚姻状态", "户口类型"]
overdue.columns = ["new_user_id", "违约"]
occupation = userinfo[["new_user_id","职业"]]
default = overdue[["new_user_id","违约"]]
data = pd.merge(occupation, default, how="outer", on="new_user_id")
plt.scatter(data["职业"], data["违约"], 1)             # scatter(x, y, [s], [c], **kwargs) [s]:可选参数，一个数或一个数组，设置每个散点的大小   [c]:可选参数，一个数或一个数组，设置每个散点的颜色
# plt.xlabel('x')  # 横坐标轴标题
# plt.ylabel('y')  # 纵坐标轴标题
plt.show()
'''

# 散点气泡图
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决Matplotlib坐标轴负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

userinfo = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\userinfo_train.csv")
overdue = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\overdue_train.csv")
userinfo.columns = ["new_user_id", "性别", "职业", "教育程度", "婚姻状态", "户口类型"]
overdue.columns = ["new_user_id", "违约"]
occupation = userinfo[["new_user_id","职业"]]
default = overdue[["new_user_id","违约"]]
data = pd.merge(occupation, default, how="outer", on="new_user_id")
size = data.groupby(["职业","违约"])['new_user_id'].agg(['count']).reset_index()
plt.scatter(size["职业"], size["违约"], size['count']/100)
plt.show()
'''
