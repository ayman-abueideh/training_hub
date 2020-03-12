import imageio
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
from PIL import Image

fig=plt.figure()
row=2
column=2

img_path='./Screenshot from 2020-03-11 14-34-34.png'

img=imageio.imread(img_path)
img=img.transpose(2,0,1)[0]
ax=fig.add_subplot(row,column,1)
ax.imshow(img,cmap='gray')
im=Image.fromarray(img)
im.save('image.png')
down_sampled=ndi.zoom(img,zoom=2)

ax1=fig.add_subplot(row,column,2)
ax1.imshow(down_sampled,cmap='gray')

im=Image.fromarray(down_sampled)
im.save('image1.png')

print(img.shape,down_sampled.shape)
up_sampled=ndi.zoom(img,zoom=4)

ax2=fig.add_subplot(row,column,3)
ax2.imshow(up_sampled,cmap='gray')

plt.show()
