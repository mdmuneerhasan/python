import sys
from math import inf

import numpy as np

nodes: int = 2
edges: int = 1
adjList = {}
visited = []


def dfs(src: int):
    ans: int = inf
    stack = []

    stack.append(src)
    visited[src]=0
    while len(stack) > 0:
        top: int = stack.pop()
        for  x in adjList[top]:
            if visited[x] > visited[top]+1:
                visited[x]=visited[top]+1
                stack.append(x)
    return int(visited[nodes])


def solve():
    global nodes
    global edges
    global adjList
    global visited
    adjList.clear()

    nodes, edges = map(int, input().split())

    visited = np.array(np.ones(nodes+2)*inf)
    for i in range(edges):
        key, value = map(int, input().split())
        if key not in adjList.keys():
            adjList[key] = []
        if value not in adjList.keys():
            adjList[value] = []
        adjList[key].append(value)
        adjList[value].append(key)
    # print(nodes)
    # print(edges)
    # print(visited)
    # print(adjList)

    print(dfs(1, -1))

    return


test = int(input())

for i in range(test):
    solve()
