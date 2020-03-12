import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import imageio
from PIL import Image
fig=plt.figure()
row=3
column=2

mat=[
    [[1,0,0],
    [0,1,0],
    [0,0,1]],

    [[.8,0,-20],
    [0,.8,-10],
    [0,0,1]],

    [[1,0,0],
    [0,1,0],
    [0,0,1]],

    [[1,0,0],
    [0,1,0],
    [0,0,1]]
]

img_path='./images/Screenshot from 2020-03-11 14-34-34.png'

img=imageio.imread(img_path)
img=img.transpose(2,0,1)[0]
ax=fig.add_subplot(row,column,1)
ax.imshow(img,cmap='gray')


com=ndi.center_of_mass(img)
d0=com[0]-90
d1=com[1]-90
xfm_shift=ndi.shift(img,shift=[d0,d1])

im=Image.fromarray(xfm_shift)
im.save('./images/image2.png')


ax1=fig.add_subplot(row,column,2)
ax1.imshow(xfm_shift,cmap='gray')

xfm_rotate=ndi.rotate(img,angle=-30,axes=(0,1),reshape=False)
ax2=fig.add_subplot(row,column,3)
ax2.imshow(xfm_rotate,cmap='gray')

xfm_aff_transform=ndi.affine_transform(img,mat[1])

ax3=fig.add_subplot(row,column,4)
ax3.imshow(xfm_aff_transform,cmap='gray')

down_sampled=ndi.zoom(img,zoom=.5)

ax4=fig.add_subplot(row,column,5)
ax4.imshow(down_sampled,cmap='gray')

plt.show()
