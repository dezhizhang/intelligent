"""
案例：演示特彺预处理之归一化操作
回顾：特征工程的目的和步骤
     目的：
        利用专业的背景知识和技巧处理数据，用于提升模型的性能
     步骤：
        1. 特征提取
        2. 特征预处理
        3. 特征
        4. 特征选择
        5. 特征组合

特征预处理之归一化介绍
    目的:
        防止因量纲（单位）问题，导致特征列的方差较大，影响模型的最终结果
        所以通过公司把和列的值映射到[0,1]区间
    公式:
        x' = (当前值 - 该列最小值) / (该列最大值 - 该列最小值)
        x''=x' * (mx - ml) + ml
"""

from sklearn.preprocessing import MinMaxScaler

# 1. 准备数据集（元数据）
x_train = [
    [90, 2, 10, 40],
    [60, 4, 15, 45],
    [75, 3, 13, 46]
]

# 2. 创建归一化对像
# 参数feature_rang表示生成范围，默认为0~1之间
scaler = MinMaxScaler(feature_range=(0, 1))

# 3. 对原数据集进行归一化
x_train_new = scaler.fit_transform(x_train)

# 4. 打印结果
print(f"{x_train_new}")
