
n=int(input())
data=list(map(int,input().split()))
ans=[]

m=0
for x in data:
    m=max(m,x)
    ans.append(m-x)
m=0
for i in range(n):
    j=n-i-1
    m=max(m,data[j])
    ans[j]=min(ans[j],m-data[j])
print(sum(ans))