
import numpy as np
import matplotlib.pyplot as plt

plt.xlim(0,5)
plt.ylim(0,5)

plt.quiver([0],[0],[2],[1],angles='xy',scale_units='xy',scale=1)
plt.grid()
plt.show()


