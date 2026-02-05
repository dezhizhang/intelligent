import pandas as pd
import numpy as np

prices = pd.Series([102.3, 103.5, 105.1, 104.8, 106.2, 107.0, 106.5, 1081.1,
                    109.3, 110.2], index=pd.date_range('2023-01-01', periods=10))


# print("每日收益率",prices.pct_change())

# print("每日收益率",prices.pct_change())
# print("收益率最高和最低",prices.pct_change().idxmax())
print("波动率",prices.pct_change().std())










