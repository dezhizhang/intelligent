# def gen_func():
#     yield 1
#
#
# def func():
#     return 1
#
# if __name__ == '__main__':
#     gen = gen_func()
#     re = func()
#     print(next(gen))
#

# def gen_func():
#     yield 1
#
# def func():
#     return 1
#
# if __name__ == '__main__':
#     gen = gen_func()
#
#     for value in gen:
#         print(value)
#

# def gen_func():
#     yield 1
#
# if __name__ == '__main__':
#     gen = gen_func()
#     for value in gen:
#         print(value)


def gen_fib(index):
    n,a,b = 0,0,1
    while n < index:
        yield b
        a,b = b,a+b
        n += 1

if __name__ == '__main__':
    gen = gen_fib(10)

    for fib in gen:
        print(fib)

