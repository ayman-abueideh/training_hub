import numpy as np
import matplotlib.pyplot as plt
import pydicom

image_path='./images/00e42241-12a0-490a-b856-db3e4ab41104.dcm'

img=pydicom.dcmread(image_path)

img_stack  = [img.pixel_array*i*10 for i in range(101) if i >0]
np_stack=np.stack(img_stack)
# print(np_stack.shape)
# fig=plt.figure()
# axes=fig.add_subplot(111)
# for i in range(100):
#     im=img_stack[i]
#     axes.imshow(im,cmap='gray')
#     axes.axis('off')
#
# plt.show()
fig, axes = plt.subplots(nrows=1, ncols=4)
for ii in range(4):
    im = img_stack[ii * 4]
    axes[ii].imshow(im, cmap='gray')
    axes[ii].axis('off')
plt.show()
