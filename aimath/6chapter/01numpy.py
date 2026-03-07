class Matrix:
    def __init__(self, data):
        """
            初始化矩阵
            :param data: 用于初始化矩阵的数据列表
        """

        if not data or not data[0]:
            raise ValueError("数据不能为空")
        self.rows = len(data)
        self.cols = len(data[0])

        if any(len(r) != self.cols for r in data):
            raise ValueError("每一行长度不一致")
        self.data = data

    def __str__(self):
        """返回矩阵的字符串表示形式"""
        return '\n' + '\n'.join([' '.join(map(str, row)) for row in self.data]) + '\n'

    def __repr__(self):
        """返回字符串表过形式"""
        return 'repr'

    def __sub__(self, other):
        """矩阵的减法"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("矩阵尺寸不匹配，不法进行减法")

        result = Matrix([[0 for _ in range(self.cols)] for _ in range(self.rows)])

        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __add__(self, other):
        """实现矩阵加法"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("矩阵尺寸不匹配，无法进行加法")
        return Matrix([[self.data[i][j] + other[i][j] for j in range(self.cols)] for i in range(self.rows)])
