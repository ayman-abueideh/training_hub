import pydicom
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import imageio

rows=3
columns=2

image_path='./images/00e42241-12a0-490a-b856-db3e4ab41104.dcm'
image_path1='./images/1_NZkRKaGnJiUMnfqDkgq3cQ.jpeg'
image_path2='./images/Screenshot from 2020-03-10 15-10-42.png'
img=pydicom.dcmread(image_path,force=True)
np_array=img.pixel_array
np_array=imageio.imread(image_path2)
fig=plt.figure()

ax=fig.add_subplot(rows,columns,1)
ax.imshow(np_array,cmap='gray')

hist=ndi.histogram(np_array,min=0,max=255,bins=256)

ax1=fig.add_subplot(rows,columns,2)
ax1.plot(hist)

cdf=hist.cumsum()/hist.sum()
ax2=fig.add_subplot(rows,columns,4)
ax2.plot(cdf)


flatten=np_array.flatten()
result=np.array(list(map(lambda x: 1 if x>122 else 0 ,list(flatten))))
# print(list(result))

# np_masked=result.reshape(np_array.shape)
np_masked=np.where(np_array>=145,np_array,0)
# np_masked=ndi.binary_erosion(np_masked,iterations=5)
ax3=fig.add_subplot(rows,columns,3)
ax3.imshow(np_masked,cmap='gray')

np_masked=np.where(np_array>=64,np_array,0)
np_masked1=np.where(np_array>=64,np_array,0)
np_masked2=np.where(1,np_masked& ~np_masked1,0)
# np_masked=ndi.binary_erosion(np_masked,iterations=5)
ax4=fig.add_subplot(rows,columns,5)
ax4.imshow(np_masked2,cmap='gray')
plt.show()
