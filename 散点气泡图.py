# -*- coding = utf-8 -*-
# @Software: Pycharm

#  散点图
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
userinfo = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\userinfo_train.csv")
overdue = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\overdue_train.csv")
userinfo.columns = ["new_user_id", "性别", "职业", "教育程度", "婚姻状态", "户口类型"]
overdue.columns = ["new_user_id", "违约", "评分"]
occupation = userinfo[["new_user_id","职业"]]
default = overdue[["new_user_id","评分"]]
data = pd.merge(occupation, default, how="outer", on="new_user_id")
plt.scatter(data["职业"], data["评分"], 1)


# 散点气泡图
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
userinfo = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\userinfo_train.csv")
overdue = pd.read_csv("D:\\Python\\Machine_Learning\\数据\\overdue_train.csv")
userinfo.columns = ["new_user_id", "性别", "职业", "教育程度", "婚姻状态", "户口类型"]
overdue.columns = ["new_user_id", "违约","评分"]
occupation = userinfo[["new_user_id","职业"]]
default = overdue[["new_user_id","违约"]]
data = pd.merge(occupation, default, how="outer", on="new_user_id")
size = data.groupby(["职业","违约"])['new_user_id'].agg(['count']).reset_index()
plt.scatter(size["职业"], size["违约"], size['count']/100)
'''

