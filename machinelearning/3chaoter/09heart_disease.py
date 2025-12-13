import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
import joblib


heart_disease_data = pd.read_csv("heart_disease.csv")

#数据处理
heart_disease_data.dropna(inplace=True)

heart_disease_data.info()

# 数据集的划分
X = heart_disease_data.drop("是否患有心脏病",axis=1)
Y = heart_disease_data["是否患有心脏病"]

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=0)


#数值型特征
numerical_features = ["年龄","静息血压","胆固醇","最大心率","运动后的ST下降","主血管数量"]
# 类别型特征
categorical_features = ["胸痛类型","静息心电图结果","峰值ST段的斜率","地中海贫血"]
# 二元特征
binary_features = ["性别","空腹血糖","运动性心绞痛"]



columnTransformer = ColumnTransformer(
    transformers=[
        ("num",StandardScaler(),numerical_features),
        ("cat",OneHotEncoder(drop="first"),categorical_features),
        ("bin","passthrough",binary_features),
    ]
)

# 特征转换
x_train = columnTransformer.fit_transform(X_train)
x_test = columnTransformer.transform(X_test)

# 创建模型
knn = KNeighborsClassifier(n_neighbors=3)

# 模型训练
knn.fit(x_train,y_train)
y_pred = knn.score(x_test,y_test)

# 保存模型
joblib.dump(value=knn, filename="knn_model")








