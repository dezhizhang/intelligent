import jieba.posseg as pseg


def dm01():
    content = "传智教育是一家上市公司,旗下有黑马程序员品牌。我是在在黑马这里学习人工智能"
    result = pseg.lcut(content)
    print(f"result:{result}")


if __name__ == "__main__":
    dm01()