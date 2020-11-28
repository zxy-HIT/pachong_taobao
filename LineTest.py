from scipy.spatial.transform import Rotation as R
import numpy as np
import pandas as pd
import cv2



df_news = pd.read_table('data/0_edge.txt',header=None)
objects = pd.read_table('data/0_box.txt', header=None)

print(objects)
print(objects.index)

img = cv2.imread('data/0_rgb.png',1)

for object in objects.index:
    pt1 = np.array(objects.loc[object].values[0:2], dtype=int)
    pt2 = np.array(objects.loc[object].values[2:4], dtype=int)
    print(pt1)
    print(pt2)
    pt1 = tuple(pt1)
    pt2 = tuple(pt2)
    zipped = zip(pt1,pt2)
    mapped = map(sum, zipped)
    print(mapped)
    sum = tuple(mapped)

    boxcolor = (255, 0, 0)
    cv2.rectangle(img,pt1,sum,boxcolor,2)


for ii in df_news.index:
    pt1 = np.array(df_news.loc[ii].values[0:2], dtype=int)
    pt2 = np.array(df_news.loc[ii].values[2:4], dtype=int)
    pt1 = tuple(pt1)
    pt2 = tuple(pt2)


    linecolor = (0, 0, 255)
    # print(pt1)
    cv2.line(img, pt1, pt2, (0, 0, 255), 1)
cv2.imshow('line', img)
cv2.waitKey()

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
