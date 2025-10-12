import  pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "id":[1,2,3,4,5],
        "name":["tom","jack","alice","bob",'allen'],
        "age":[15,17,20,26,30],
        "score":[60.5,80,30.6,70,83.5]
    }
)

# print(df.index)
# print(df.columns)

# 获取值
print("获取值",df.values)
print("维度",df.ndim)
print("数据类型",df.dtypes)
print("形状",df.shape)



