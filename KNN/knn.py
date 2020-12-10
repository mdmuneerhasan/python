import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')
dfx = pd.read_csv('xdata.csv')
dfy = pd.read_csv('ydata.csv')
X = dfx.values
Y = dfy.values


X = X[:,1:]
Y = Y[:,1:].reshape((-1,))
print(X)
print(Y)
def dist(x1,x2):
    return np.sqrt(sum((x1 - x2) ** 2))

def knn(X, Y, queryPoint, k=3):
    vals = []
    m = X.shape[0]

    for i in range(m):
        d = dist(queryPoint, X[i])
        vals.append((d, Y[i]))

    vals = sorted(vals)
    vals = vals[:k]
    vals = np.array(vals)
    new_vals = np.unique(vals[:, 1], return_counts=True)
    index = new_vals[1].argmax()
    pred = new_vals[0][index]

    return pred

x = knn(X,Y,[0,0])
print(x)
