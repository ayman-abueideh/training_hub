
#see numpy cheetcheat

import numpy as np
import matplotlib.pyplot as plt

np_2d=np.array([
    [1,2,3,4,5,6,7,8,9],
    [9,8,7,6,5,3,2,1,4]
])

np_2d_1=np.array([
    [1,3,3,4,5,6,7,8,9],
    [9,8,7,6,5,3,2,1,4]
])

np_2d_2=np_2d_1.reshape(9,2)
print('np.multiply',np.multiply(np_2d,np_2d_1))
print('np_2d.dot',np_2d.dot(np_2d_2))
print('np.kron',np.kron(np_2d_2.T,np_2d_1).shape)# cross product
print('np.tensordot',np.tensordot(np_2d_2.T,np_2d_1,axes=0).shape)
np_2d.copy()[0][0]=0
print('np_2d.copy',np_2d.copy())
# memory address
print('np_2d.dataa',np_2d.data)
# shape of array
print('np_2d.shape',np_2d.shape)
#type of data
print('np_2d.shape',np_2d.dtype)
#stride of array
print('np_2d.strides',np_2d.strides)

print('np_2d.size',np_2d.size)

print('np_2d.ndim',np_2d.ndim)
print('np_2d.flags',np_2d.flags)
print('np_2d.itemsize',np_2d.itemsize)
print('np_2d.nbytes',np_2d.nbytes)

print('np.empty',np.empty((3,2)))
print('np.linespace',np.linspace(3,3,1))
np.save('np_2D.txt',np_2d)
print(len(np_2d[0]))
print('np.transpose',np.transpose(np_2d_1).T)

print('np.histogram',np.histogram(np_2d))
plt.hist(np.histogram(np_2d))
# plt.show()
np_2d=np.array([
    [1,2,3,4,5,6j,7,8,9],
    [9,8,7,6,5,3,2,1,4]
])
print('np.real',np.real(np_2d))
print('np.imag',np.imag(np_2d))
print('np.real_if_close',np.real_if_close(np_2d))

def myfunc(a,b):
  if a > b:
     return a - b
  else:
     return a + b

print('np.vectorize',np.vectorize(myfunc))

print('np.r_',np.r_[np_2d_2.T,np_2d_1])
print('seperate')
print('np.c_',np.c_[np_2d_2.T,np_2d_1])
print('np.mgrid',np.mgrid[1:11:1, -12:-3:1])
print('np.ogrid',np.ogrid[1:11:2, -12:-3:3])
print('np.hstack',np.hstack((np_2d_2.T,np_2d_1)))
print('np.vstack',np.vstack((np_2d_2.T,np_2d_1)))
print('np.hsplit',np.hsplit(np.hstack((np_2d_2.T,np_2d_1)),6))
print('np.vsplit',np.vsplit(np.vstack((np_2d_2.T,np_2d_1)),4))
print('np_2d_1.reshape',np_2d_1.reshape(3,6))
print('np.resize',np.resize(np_2d_1,(6,2)))
np_matrix=np.matrix(np.random.random((5,5)))
print('np.matrix',np_matrix)

