C1=[[0,0],[1,1],[2,2],[-1,1],[1,2],[2,1],[3,3],[0,2],[1,3],[3,1],[1,1],[2,3],[2,2],[1,-1],[2,2],[3,1]]

C2=[[10,10],[9,9],[11,11],[11,12],[13,9],[10,10],[9,9],[11,13],[11,12],[13,9],[10,11],[9,8],[11,10],[11,9],[11,9]]




def KNearestNiebhbour(point,k=3):
    dist=[]
    for i in range(len(C1)):
        d=((point[0]-C1[i][0])*(point[0]-C1[i][0])+(point[1]-C1[i][1])*(point[1]-C1[i][1]))
        dist.append([d,"c1"])

    for i in range(len(C2)):
        d=((point[0]-C2[i][0])*(point[0]-C2[i][0])+(point[1]-C2[i][1])*(point[1]-C2[i][1]))
        dist.append([d,"c2"])

    dist.sort()
    c1=0
    c2=0
    for i in range(k):
        if dist[i][1]=='c1':
            c1+=1
        else:
            c2+=1

    if c1>=c2:
        return "C1 class"
    else:
        return "C2 class"


print(KNearestNiebhbour([1,1]))


