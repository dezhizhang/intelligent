import numpy as np
import pandas as pd


def dm01_data_preprocess():
    # 1. 读取csv文件，获取到df对像
    churn_df = pd.read_csv('../assets/churn.csv')

    # 2. 因为churn和gender列是字符串，需要进行one-hot编码
    churn_df = pd.get_dummies(churn_df,columns=['Churn','gender'])

    # 3. 删除one-hot处理后的冗余列
    churn_df.drop(['Churn_No','gender_Male'],axis=1,inplace=True)
    # churn_df.info()
    # print(churn_df.head(5))

    # 4. 修改列表将Churn_Yes-> Flag 充当标签列
    churn_df.rename(columns={"Churn_Yes":"flag"},inplace=True)

    # 5. 查看数据值分布
    print(churn_df.flag.value_counts())



if __name__ == '__main__':
    dm01_data_preprocess()
