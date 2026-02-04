import pandas as pd
import numpy as np
temperature = pd.Series(
    [28,31,29,32,30,27,33],
    index=['周一','周二','周三','周四','周五','周六','周日']
)

num = temperature[temperature > 30].count()

print("超过30度的天数",num)
print("平均温度",temperature.mean())
print("排序后的结果",temperature.sort_values(ascending=False))

t1 = temperature.diff().abs()


print("温度变化的最大的两天",t1.sort_values(ascending=False).keys()[:2])


