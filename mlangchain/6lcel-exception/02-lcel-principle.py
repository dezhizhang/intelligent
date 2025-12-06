class Expression:
    """表过式基类，所有组件都继承自此类"""

    def __init__(self,func):
        self.func = func

    def __call__(self,value):
        return self.func(value)

    def __or__(self, other):
        """重载 | 运算符，返回一个新的串联表达式"""
        return Expression(lambda x: other(self(x)))



def upper(s):
    return s.upper()

def lower(s):
    return s.lower()

def reverse(s):
    return s[::-1]

Upper = Expression(upper)
Lower = Expression(lower)
Reverse = Expression(reverse)

result = Expression(lambda x:x) | Upper | Reverse

print(result("hello world"))

