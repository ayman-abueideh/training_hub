import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import imageio

fig=plt.figure()
row=3
column=2
img_path='./images/Screenshot from 2020-03-11 11-31-31.png'
img=imageio.imread(img_path)
img=img.transpose(2,0,1)[0]

ax=fig.add_subplot(row,column,1)
ax.imshow(img,cmap='gray')

img_median=ndi.median_filter(img,size=3)
ax1=fig.add_subplot(row,column,2)
ax1.imshow(img_median,cmap='gray')

img_mask=np.where(img_median>100,1,0)

ax2=fig.add_subplot(row,column,3)
ax2.imshow(img_mask,cmap='rainbow')

labels=ndi.label(img_mask)
masked_label=np.where(labels[0]==10,1,0)
boxes=ndi.find_objects(labels[0])

overlay=np.where(labels[0]==10,labels[0][128],np.nan)
print(img.shape)
ax3=fig.add_subplot(row,column,4)
ax3.imshow(masked_label,cmap='rainbow')
ax.imshow(overlay)


cmos=ndi.center_of_mass(img,labels[0],index=range(44))

ax4=fig.add_subplot(row,column,5)

print(cmos)
for c1,c2 in cmos:
    ax4.scatter(c2,c1,s=100)
plt.show()


var_all=ndi.variance(img,labels=None,index=None)
hist_all=ndi.histogram(img,min=0,max=1,bins=256)

var_labels=ndi.variance(img,labels=labels[0],index=None)
hist_labels=ndi.histogram(img,min=0,max=1,bins=256,labels=labels[0])

var_label=ndi.variance(img,labels=labels[0],index=[10])
hist_label=ndi.histogram(img,min=0,max=1,bins=256 ,labels=labels[0],index=1)

# print('var all',var_all,'hist_all',hist_all)
# print('var labels',var_labels,'hist labels',hist_labels)
# print('var label',var_label,'hist label',hist_label)
