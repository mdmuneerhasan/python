from matplotlib import pyplot as plt


data=[[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
center =[[]]

k = 3
color = ['green', 'red', 'blue']


clusters = {}
for i in range(k):
    points = []
    cluster = {
        'center': center,
        'points': points,
        'color': color[i]
    }
    clusters[i] = cluster


def distanc(v1, v2):
    return np.sqrt(np.sum((v1 - v2) ** 2))


# E-step : estimated step
def assignPointToClusters(clusters):
    for ix in range(X.shape[0]):
        dist = []
        curr_x = X[ix]
        for kx in range(k):
            d = distanc(curr_x, clusters[kx]['center'])
            dist.append(d)
        current_cluster = np.argmin(dist)
        clusters[current_cluster]['points'].append(curr_x)


# M-step
def updateCluster(clusters):
    for kx in range(k):
        pts = np.array(clusters[kx]['points'])

        if pts.shape[0]>0:
           new_u = pts.mean(axis=0)
           clusters[kx]['center']=new_u
           clusters[kx]['points']=[]




def plotCluster(cluseters,name):
    plt.clf()
    for kx in range(k):
        pts = np.array(clusters[kx]['points'])
        try:
            plt.scatter(pts[:, 0], pts[:, 1], color=clusters[kx]['color'])
        except:
            pass
        uk = cluseters[kx]['center']
        plt.scatter(uk[0], uk[1], color="black", marker="*")
        plt.savefig('graph2'+name)

for i in range(10):
    assignPointToClusters(clusters)
    plotCluster(clusters,str(i))
    updateCluster(clusters)

