"""知识库"""
import os


def check_md5():
    """检查传入的md5字符串是否已经被处理过了"""
    if not os.path.exists("data"):
        os.mkdir("data")
    pass

def save_md5():
    """将传入的md5字符串，记录到文件内保存"""

def get_string_md5():
    """将传入的字符串转换成md5字符串"""
    pass

class KnowledgeBaseService(object):
    def __init__(self):
        self.chroma = None
        self.spliter = None

    def upload_by_str(self,data,filename):
        pass
