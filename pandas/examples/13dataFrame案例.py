import pandas as pd

data = {
    "产品名称":['A','B','C','D'],
    "单价":[100,150,200,120],
    "销量":[50,30,20,40]
}

df = pd.DataFrame(data)
print(df)
# 计算每个产品的销售额
df['总销售额'] = df['单价'] * df['销量']

print( df['总销售额'])

df.nlargest(1,['总销售额'])