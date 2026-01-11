import matplotlib.pyplot as plt

languages = ["python","java",'js/ts','other']
counts = [30,25,20,25]

plt.pie(counts, labels=languages)
plt.show()

