import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_classification

X, Y = make_classification(n_classes=2, n_samples=400, n_clusters_per_class=1, random_state=3, n_features=2,
                           n_informative=2, n_redundant=0)
Y[Y==0]=-1
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.savefig("graph1")


class SVM:
    def __int__(self, C=1.0):
        self.C = C
        self.W = 0
        self.b = 0
    def init(self,c=1.0):
        self.C=1.0

    def hingeLoss(self, W, b, X, Y):
        loss = 0.0
        loss += 0.5 * np.dot(W, W.T)
        m = X.shape[0]

        for i in range(m):
            ti = Y[i] * (np.dot(W, X[i].T) + b)
            loss += self.C * max(0, 1 - ti)

        return loss

    def fit(self, X, Y, batch_size=100, learning_rate=0.001,maxItr=300):
        no_of_featture = X.shape[1]
        no_of_sample = X.shape[0]

        n = learning_rate
        c = self.C

        W = np.zeros((1, no_of_featture))
        bias = 0
        print(self.hingeLoss(W, bias, X, Y))

        losses=[]

        for i in range(maxItr):
            l=self.hingeLoss(W,bias,X,Y)
            losses.append(l)
            ids=np.arange(no_of_sample)
            np.random.shuffle(ids)
            for batch_start in range(0,no_of_sample,batch_size):
                gradw=0
                gradb=0
                for j in range(batch_start,batch_start+batch_size):
                    if j<no_of_sample:
                        i=ids[j]
                        ti=Y[i]*(np.dot(W,X[i].T)+bias)
                        if ti > 1:
                            gradw+=0
                            gradb+=0
                        else:
                            gradw+=c*Y[i]*X[i]
                            gradb+=c*Y[i]
                W=W-n*W+n*gradw
                bias=bias+n*gradb
            self.W=W
            self.b=bias
            return W,bias,losses






mySVM = SVM()
mySVM.init()
W,bias,losses=mySVM.fit(X,Y)
for l in losses:
    for l1 in l:
        for l2 in l1:
            print(l2)
plt.clf()
# plt.plot(losses)
plt.savefig("graph2")