import jieba
from tensorflow.keras.preprocessing.text import  Tokenizer
import joblib



def dm_onehot_gen():
    # 1. 准备语料
    vocabs = {"周杰伦","陈奕迅","王力宏","李宗盛","吴亦凡","鹿晗"}
    # 2. 实例化分词器
    mytokenizer = Tokenizer()
    # 3. 训练分词器
    mytokenizer.fit_on_texts(vocabs)

    #4. 检验训练效果
    print(mytokenizer.word_index)
    print(mytokenizer.index_word)

    #5. 查找每个单词的one-hot编码
    for vocab in vocabs:
        # 初始化一个全零的列表，长度为len(vocabs)
        zero_list = [0] * len(vocabs)

        idx = mytokenizer.word_index[vocab] - 1
        zero_list[idx] = 1
        print(f"当前单{vocab}的one-hot编码是{zero_list}")

    mypath = "./mytokenizer"
    joblib.dump(mytokenizer,mypath)
    print(f"mytokenizer已保存")

def use_onehot():
    #1.  准备语料
    vocabs = {"周杰伦", "陈奕迅", "王力宏", "李宗盛", "吴亦凡", "鹿晗"}
    mypath = "./mytokenizer"
    tokenizer = joblib.load(mypath)
    token = '王力宏'
    zero_list = [0] * len(vocabs)
    idx = tokenizer.word_index[token] - 1
    zero_list[idx] = 1
    print(f"当前：{zero_list}")


if __name__ == "__main__":
    use_onehot()