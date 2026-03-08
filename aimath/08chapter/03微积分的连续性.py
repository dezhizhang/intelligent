# from sympy import *
#
#
# x = symbols('x')
# k = symbols('k')
# a = symbols('a')
# b = symbols('b')
# c = symbols('c')
# n = symbols('n')
#
# functions = [
#     k,
#     x,
#     b * x + c,
#     x**n
# ]
#
#
# for f in functions:
#     print(f"lim{f} 极限:{limit(f,x,a)}")
#

from sympy import *

x = Symbol('x')
n = Symbol('n')

f = x ** n

lmt = limit(f.subs(n,2), x, 0)
print(f"lim({f}) x > 0 极限:{lmt}")
