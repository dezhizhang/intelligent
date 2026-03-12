import pandas as pd
import numpy as np
from  sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error,root_mean_squared_error
from sklearn.linear_model import Ridge,RidgeCV
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

# 2. 数据的预处理
x_train,x_test,y_train,y_test = train_test_split(data,target,test_size=0.2,random_state=23)

# 3. 创建标准化对像
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)


# 4. 训练模型
estimator = LinearRegression(fit_intercept=True)
estimator.fit(x_train,y_train)

# 打印计算模型
# print(f"权重:{estimator.coef_}")
# print(f"偏置:{estimator.intercept_}")


# 5. 模型预测
y_pre = estimator.predict(x_test)
print(f"预测结果:{y_pre}")

# 5. 模型评估
print(f"均方误关:{mean_squared_error(y_test, y_pre)}")
print(f"均方根误差:{root_mean_squared_error(y_test, y_pre)}")
print(f"平均绝对误差:{mean_squared_error(y_test,y_pre)}")




