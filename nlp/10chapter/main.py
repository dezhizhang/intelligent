import jieba


def dm01():
    content = "传智教育是一家上市公司,旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
    # result = jieba.lcut(content)
    # print(f"result:{list(result)}")
    # 加载自定义词典
    jieba.load_userdict("./userdict.txt")
    result = jieba.lcut(content)
    print(f"result:{result}")


if __name__ == "__main__":
    dm01()

