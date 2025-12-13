import pandas as pd
import seaborn as sns
from sklearn.metrics import confusion_matrix


# 定义类别标签
labels = ["猫","狗"]
y_true = ["猫","狗","猫","狗","猫","狗","猫","狗","猫","狗","猫","狗"]
y_pred = ["猫","猫","猫","狗","猫","狗","猫","狗","狗","狗","猫","猫"]

matrix = confusion_matrix(y_true,y_pred,labels=labels)
print(matrix)

# 定义
colum = pd.DataFrame(matrix,index=labels,columns=labels)
print(colum)

sns.heatmap(matrix,annot=True,fmt="d",cmap="Greens")



