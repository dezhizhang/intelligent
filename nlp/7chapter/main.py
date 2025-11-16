import jieba

def dm01():
    content = "数擎科技有限公司"
    result = jieba.cut_for_search(content)
    print(f"result:{list(result)}")

if __name__ == "__main__":
    dm01()
