import matplotlib.pyplot as plt

data = [(160,50),(170,60),(165,55),(180,75),(175,70)]

height = [item[0] for item in data]
weight = [item[0] for item in data]


plt.scatter(height,weight)
plt.xlabel('Height')
plt.show()



