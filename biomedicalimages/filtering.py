import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndi
import imageio
image_path1='./images/1_NZkRKaGnJiUMnfqDkgq3cQ.jpeg'
image_path2='./images/Screenshot from 2020-03-10 15-10-42.png'

fig=plt.figure()
rows=2
column=2
img=imageio.imread(image_path2)
img1=img.transpose(2,0,1)
ax=fig.add_subplot(rows,column,1)
ax.imshow(img1[0],cmap='gray')

weights=np.array([[
    [1,1,1],
    [1,1,1],
    [1,1,1]],

    [[1,2,1],
    [0,0,0],
    [-1,-2,-1]],

    [[1,1,1],
    [0,0,0],
    [1,1,1]],

    [[1,0,-1],
    [2,0,-2],
    [1,0,-1]],

    [[1,0,1],
    [1,0,1],
    [1,0,1]]
])


print(img.shape,weights.shape)
c=1
img_filt=ndi.convolve(img1[0],list(weights[1]),mode='constant',cval=0)
img_hfilt=ndi.convolve(img1[0],list(weights[1]),mode='constant',cval=0)
img_vfilt=ndi.convolve(img1[0],list(weights[3]),mode='constant',cval=0)
img_hvfilt=np.sqrt(np.square(img_hfilt)+np.square(img_vfilt))
print(img_hvfilt.dtype,img_filt.dtype)

ax1=fig.add_subplot(rows,column,2)
ax1.imshow(img_hfilt.astype('uint8'),cmap='gray')

im_gaussian=ndi.gaussian_filter(img1[0],sigma=2)

ax2=fig.add_subplot(rows,column,3)
ax2.imshow(im_gaussian,cmap='gray')

im_gaussian_in=np.where(im_gaussian>145,1,0)
im_sobel=ndi.sobel(img,axis=0)

ax3=fig.add_subplot(rows,column,4)
ax3.imshow(im_sobel,cmap='gray')



plt.show()
