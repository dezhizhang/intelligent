import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x **2

def area_sum_by_rectangle(start_x,end_x):
    n_pre_unit = 50
    n = n_pre_unit * (end_x - start_x)
    width = 1 / n_pre_unit
    x_values = np.linspace(start_x, end_x, n + 1)

    area_sum = 0
    for i in range(n):
        area_sum += f(x_values[i]) * width
    return area_sum


print(area_sum_by_rectangle(0,3))





# a,b = 0,3
# n=300
#
# x_values = np.linspace(a, b, n + 1)
#
# width = (b- a) / n
#
# area_sum = 0
# for i in range(n):
#     area_sum += f(x_values[i])
#
# x = np.linspace(a, b, 100)
# y = f(x)
#
# fig,ax = plt.subplots()
# ax.plot(x,y)
#
# for i in range(n):
#     rect_x = [x_values[i],x_values[i],x_values[i+1],x_values[i+1]]
#     rect_y = [0,f(x_values[i]),f(x_values[i]),0]
#     plt.plot(rect_x,rect_y,'g')
# plt.show()




