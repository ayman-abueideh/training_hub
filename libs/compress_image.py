import numpy as np
from scipy import linalg,sparse
from skimage import  data
import matplotlib.pyplot as plt

image=data.camera()

linalg.svdvals(image)

u,s,vh=linalg.svd(image)

A=np.dot(u[:,0:64],np.dot(np.diag(s[0:64]),vh[0:64,:]))

fig=plt.figure(figsize=(8,3))

ax=fig.add_subplot(121)

ax.imshow(image,cmap='gray')

ax2=fig.add_subplot(122)

ax2.imshow(A,cmap='gray')
plt.show()
