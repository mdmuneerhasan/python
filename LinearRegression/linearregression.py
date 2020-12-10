import matplotlib.pyplot as plt

# writing algorithm for y=3*x+7 or y=a+bx

X_train = [-3, -1, -.5, 1, 2, 3, 4, 6, 8, 96, 4, 24, 6, 86, 4, 3, 50, 60, 70, 80]
Y_train = [-2.2, 4.1, 5, 9.88, 13.8, 16.1, 19.2, 24, 32, 280, 19.1, 79.2, 25.5, 265.4, 21, 16, 151, 182, 222, 240]



def hypothesis(a,b,x):
    return a+b*x;


def find_a_and_b(X_train,Y_train):
    # a=Ey/n
    # b=Exy/Exx
    Ey=0
    EXY=0
    EXX=0
    n=len(X_train)
    meanX=0
    meanY=0
    for i in range(n):
        meanX+=X_train[i]
        meanY+=Y_train[i]
    meanX/=n
    meanY/=n
    for i in range(n):
        Ey+=Y_train[i]
        EXY+=(X_train[i]-meanX)*Y_train[i]
        EXX+=(X_train[i]-meanX)**2
        b=EXY/EXX
        a=meanY-meanX*b
    return a,b

a,b=find_a_and_b(X_train,Y_train)
print(a,b)

x = [-10,1, 2, 3, 4, 5,100]
y = []

for p in x:
    y.append(hypothesis(a,b,p))

print(x, y)

plt.scatter(X_train, Y_train)
plt.savefig("xy_cartesian_plan")
plt.plot(x,y,color='orange')
plt.savefig("xy_cartesian_plan2")
