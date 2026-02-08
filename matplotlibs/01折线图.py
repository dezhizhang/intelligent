import matplotlib.pyplot as plt
from matplotlib import rcParams


rcParams['font.family'] = ['Songti']  # 或者 'Songti SC', 'STXihei'

# 负号正常显示
rcParams['axes.unicode_minus'] = False


# 创建图表设置大小
plt.figure(figsize=(10,5))

# 要绘制的数据
month = ['1月','2月','3月','4月']
sales = [100,150,180,130]

plt.plot(month,sales)

# 添加标题
plt.title("2025年",color="red",fontsize=10)
plt.ylabel("销售额",fontsize=10)

# 显示图表
plt.show()

