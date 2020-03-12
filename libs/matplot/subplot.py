import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure(figsize=(5,5))

ax=fig.add_subplot(1,2,1)
ax.plot(np.arange(10),np.arange(10)*10)

ax1=fig.add_subplot(1,2,2)
ax1.plot(np.arange(100),np.arange(100)*10)

plt.show()
