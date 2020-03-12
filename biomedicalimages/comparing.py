import imageio
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

fig=plt.figure()
row=2
column=2

img_path='./images/image.png'
img_path1='./images/image2.png'
print()


img1=imageio.imread(img_path)
img2=imageio.imread(img_path1)
# img2=ndi.zoom(img2,zoom=.5)
img3=img2-img1

ax1=fig.add_subplot(row,column,1)
ax1.imshow(img1,cmap='gray')

ax2=fig.add_subplot(row,column,2)
ax2.imshow(img2,cmap='gray')

ax3=fig.add_subplot(row,column,3)
ax3.imshow(img3,cmap='gray')

plt.show()
# plt.show()
# plt.show()
