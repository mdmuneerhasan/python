import pandas as pd
import numpy as np
n=0
max_wt=0
dp=[]
wt=[]
val=[]
def solve(max_wt ):
    if max_wt == 0:
        return 0
    if dp[max_wt]!=-1:
        return dp[max_wt]
    dp[max_wt]=0;
    for i in range(n):
        if max_wt >= wt[i]:
            dp[max_wt]=max(dp[max_wt],solve(max_wt-wt[i])+val[i])
    return dp[max_wt]

n,max_wt=map(int,input().split())
dp=[-1]*(max_wt+2)
wt=list(map(int,input().split()))
val=list(map(int,input().split()))


print(solve(max_wt))