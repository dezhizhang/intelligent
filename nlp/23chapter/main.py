import fasttext

def dm_fasttext_train_save_load():
    model = fasttext.train_unsupervised("./fil9")
    print("训练向量ok")

    # 保存模型
    model.save_model("./fil9.bin")

    # 3. 加载模型
    model = fasttext.load_model("./fil9.bin")
    print("model",model)

def dm_fasttext_get_word_vector():
    model = fasttext.load_model("./fil9.bin")

    result = model.get_word_vector("the")
    print(f"result:{result} shape:{result.shape}")




if __name__ == "__main__":
    dm_fasttext_get_word_vector()

