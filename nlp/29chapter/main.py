

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def dm_label_countplot():
    train_data = pd.read_csv(filepath_or_buffer="./train.tsv",sep='\t')
    dev_data = pd.read_csv(filepath_or_buffer='./dev.tsv',sep='\t')

    sns.countplot(x='label',data=train_data)

    plt.title("train_label")
    plt.show()

    sns.countplot(x="label",data=dev_data)

    plt.title('dev_label')
    plt.show()



if __name__ == "__main__":
    dm_label_countplot()
