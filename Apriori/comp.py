



n=int(input())

s=input()
s=s.replace('-',' ')
lst=s.split(' ')


ans=0

for x in lst:
    ans=max(ans,len(x))

print(ans)

