from scipy import sparse,linalg
import scipy
import numpy as np

np_matrix=np.matrix(np.random.random((5,5)))
np_vector=np.array([1,2,1])
np_iden=np.eye(3,k=0)
# np_iden[0][0]=2
# np_iden[1][1]=2
# np_iden[2][0]=2
print('np.eye',np_iden)

print('sparse.csr_matrix',sparse.csr_matrix(np_iden))
print('sparse.csc_matrix',sparse.csc_matrix(np_iden))
print('sparse.dok_matrix',sparse.dok_matrix(np_iden))
print('sparse.bsr_matrix',sparse.bsr_matrix(np_iden))
print('sparse.coo_matrix',sparse.coo_matrix(np_iden))
print('sparse.lil_matrix',sparse.lil_matrix(np_iden))
print('sparse.dia_matrix',sparse.dia_matrix(np_iden))

print('linalg.expm',linalg.expm(np_iden))
# print('linalg.expm2',sparse.linalg.expm2(np_iden))
# print('linalg.expm3',linalg.expm3(np_iden))
print('linalg.cosm',linalg.cosm(np_iden))
print('linalg.sinm',linalg.sinm(np_iden))
print('linalg.norm',linalg.norm(np_iden))
print('linalg.det',linalg.det(np_iden))
# print('sparse.linalg.spsolve',sparse.linalg.spsolve(np_iden,np_iden.T))
print('sparse.linalg.eig',linalg.eigvals(np_iden))
print('linallg.svd',linalg.svd(np_iden))
