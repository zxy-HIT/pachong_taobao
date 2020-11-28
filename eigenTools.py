from scipy.spatial.transform import Rotation as R
import numpy as np

print("Transform Start!")
# use [:, np.newaxis] to transform from row vector to col vector
position = np.array([0.6453529828252734, -0.26022684372145516, 1.179122068068349])[:, np.newaxis]
share_vector = np.array([0,0,0,1], dtype=float)[np.newaxis, :]
print('share_vector:\n', share_vector)
print('position:\n',position)

Rotation = np.mat([[1, 0.0011, 0.0004], [0, -0.3376, 0.9413], [0.0011, -0.9413, -0.3376]])
print(Rotation)
r = R.from_matrix(Rotation)
print('as_quat():\n',r.as_quat())
# r = R.from_matrix()
