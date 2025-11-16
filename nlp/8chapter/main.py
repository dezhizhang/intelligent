# import jieba
#
# def dm01():
#     content = "煩惱即是菩提,我暫且不提"
#     result = jieba.cut(content)
#     print(f"list:{list(result)}")
#     pass
#
# if __name__ == '__main__':
#     dm01()

import jieba

def dm01():
    content = "煩惱即是菩提,我暫且不提"
    result = jieba.cut(content)
    print(f"list:{list(result)}")

if __name__ == '__main__':
    dm01()