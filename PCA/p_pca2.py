import numpy as np
import matplotlib as plot
import matplotlib.pyplot as plt
import matplotlib.image as img
from numpy.linalg import svd
from sklearn.decomposition import PCA

img = img.imread('test.jpg')
img=img[:,:,1]
plt.imshow(img,cmap="gray")
plt.savefig('graph')



def apply_pca(dimension, img):
    covar = np.dot(img.T, img)
    U, S, V = svd(covar)
    Ured = U[:, :dimension]
    z = np.dot(img, Ured)
    return z


for i in range(1,2):
    blue_inverted = apply_pca(10*i,img)
    plt.figure()
    plt.imshow(blue_inverted,cmap="gray")
    plt.savefig('graph'+str(i))
