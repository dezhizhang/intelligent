"""为整个工程提供统一的绝对路径"""
import os

def get_project_root()-> str:
    """获取工程所在的根目录"""
    # 当前文件的绝对路径
    cur_file = os.path.abspath(__file__)
    # 获取当前文件的绝对路径
    cur_dir = os.path.dirname(cur_file)
    # 获取工程目录
    project_root = os.path.dirname(cur_dir)

    return project_root

def get_abs_path(relative_path: str) -> str:
    """根据相对路径获取绝对路径"""
    return os.path.join(get_project_root(), relative_path)

if __name__ == '__main__':
    print(get_abs_path("config/config.txt"))
