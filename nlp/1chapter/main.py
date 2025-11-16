#coding:utf-8

import jieba

def dm01():
    content = "数擎科技有限公司"
    result = jieba.cut(content,cut_all=False)
    print(f"result:{result}")

    for value in result:
        print(value)



if __name__ == '__main__':
    dm01()
