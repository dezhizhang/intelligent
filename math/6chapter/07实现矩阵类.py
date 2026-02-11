class Matrix:
    def __init__(self,data):
        """初始化矩阵"""
        if not data or not data[0]:
            raise ValueError("数据不能为空")
        self.rows = len(data)
        self.cols = len(data[0])

        if any(len(r) != self.cols for r in data):
            raise ValueError("每一行长度不一致")

        self.data = data



