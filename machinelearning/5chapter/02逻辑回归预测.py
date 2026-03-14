import pandas as pd
from sklearn.metrics import confusion_matrix


# 定义变量
#1.定义变量,记录:样本数据
y_train=['恶性','恶性','恶性','恶性','恶性','恶生','良性','良性','良性','良性']
#2.定义变量,记录:模型A的预测结果
y_pre_A=['恶性','恶性','恶性','良性','良性','良性','良性','良性','良性','良性']
#3.定义变量,记录:模型B的预测结果
y_pre_B = ['恶性','恶性','恶性','恶性','恶性','良性','良性','良性','良性']


labels = ['恶性','良性']
df_label = ['恶性(正例)','良性(反例)']

# 4. 针对于真实值(y_train)和模型A的预测结果(y_pre_A)

cm_A=confusion_matrix(y_train,y_pre_A,labels=labels)

df_A = pd.DataFrame(cm_A,index=df_label,columns=df_label)

# 针对于真实值(y_train)和模型的预测结果(y_pre_B) 搭建混淆矩阵
cm_B = confusion_matrix(y_train,y_pre_B,labels=labels)


df_B = pd.DataFrame(cm_B,index=df_label,columns=df_label)

