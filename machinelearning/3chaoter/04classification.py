import pandas as pd
import seaborn as sns
from  sklearn.metrics import confusion_matrix

# 定义标签名
labels = ["猫","狗"]
y_true = ["猫","狗","猫","狗","猫","狗","猫","狗","猫","狗","猫","狗"]
y_pred = ["猫", "猫", "猫", "狗", "猫", "狗", "猫", "狗", "狗", "狗", "猫", "猫"]

matrix = confusion_matrix(y_true, y_pred)
print(matrix)

pd.DataFrame(matrix,index=labels,columns=labels)
sns.heatmap(matrix,annot=True,fmt="d",cmap="YlGnBu")




