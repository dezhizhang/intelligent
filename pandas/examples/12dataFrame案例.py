import pandas as pd

data = {
    "姓名":["张三","李四","王五","赵六","钱七"],
    "数学":[85,92,78,88,95],
    "英语":[90,88,85,92,80],
    "物理":[75,80,88,85,90]
}

scores = pd.DataFrame(data)

# 计算每位学生的总分和平均分
scores['总分'] = scores[['数学','英语','物理']].sum(axis=1)
scores['平均分'] = scores[['数学','英语','物理']].mean(axis=1)


print(scores[(scores['数学'] >90) | (scores['英语'] > 85)])


