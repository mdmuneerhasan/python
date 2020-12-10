

a,b=map(int,input().split())

wt=[]
for i in range(101):
    wt.append(a^i)

wt.sort()


print(wt)
print(b)


