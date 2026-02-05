import numpy as np
import pandas as pd


# print(sales)

# a = pd.date_range("2022-01-01-01",periods=12,freq="MS")
# print(a)

sales = pd.Series([120, 135, 145, 160, 155, 170, 175, 175, 190, 200, 2210,
220],index=pd.date_range('2022-01-01', periods=12, freq='MS'))


# print(sales.resample('QS').mean())
# print(sales.resample('MS').sum())

# 找到销量最高的月份
print(sales.idxmax())
