import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, y = make_blobs(n_samples=500, n_features=2, centers=5, random_state=3)
kmeans = KMeans(n_clusters=5)
kmeans.fit(X, y)
centers= kmeans.cluster_centers_
plt.scatter(X[:,0],X[:,1])
plt.scatter(centers[:,0],centers[:,1],marker='*',color='orange')
plt.savefig("graph31")


