import imageio
import pydicom
import numpy as np
import matplotlib.pyplot as plt
image_path='./images/00e42241-12a0-490a-b856-db3e4ab41104.dcm'
img=pydicom.dcmread(image_path,force=True)

print(type(img))
print(img)
print(type(img.pixel_array))

# im=imageio.imread(img)
vol=np.stack([img.pixel_array,img.pixel_array*100,img.pixel_array*1000,img.pixel_array*100,img.pixel_array])
print(vol.shape)

# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.imshow(img.pixel_array*2100,cmap='gray')
# plt.show()
