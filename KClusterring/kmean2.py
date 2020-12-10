from matplotlib import pyplot as plt
import random

k = 3
dataset = [[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
cluster = [{'points': [], 'center': [2, 10]},
           {'points': [], 'center': [5, 8]},
           {'points': [], 'center': [1, 2]}, ]


def assign():
    for i in range(len(dataset)):
        dist = []
        ind = 0
        for j in range(k):
            center = cluster[j]['center'];
            d = ((dataset[i][0] - center[0]) ** 2 + (dataset[i][1] - center[1]) ** 2) ** .5
            dist.append(d)
            if (d < dist[ind]):
                ind = j
        cluster[ind]['points'].append(dataset[i])


def show():
    print()
    print(cluster)


def update():
    for i in range(k):
        pts = cluster[i]['points']
        n = len(pts)
        x = 0
        y = 0
        if n > 0:
            for j in range(n):
                x = x + pts[j][0]
                y = y + pts[j][1]
            cluster[i] = {
                'center': [x / n, y / n],
                'points': []
            }


for i in range(10):
    assign()
    show()
    update()
