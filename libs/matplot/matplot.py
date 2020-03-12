import matplotlib.pyplot as plt
import numpy as np

np_array=np.arange(11)
# print(np_array)
plt.scatter(np_array,np_array*10,label='linear')
plt.legend()
plt.show()

plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='h')
plt.xlim(2.5, 4.5)
plt.show()
