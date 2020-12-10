def winnerSquareGame(n: int) -> bool:
    dp = []
    p={}
    for i in range(n + 3):
        dp.append(False)

    j = 0
    for i in range(1, n + 3):
        if i >= (j + 1) ** 2:
            j += 1
            p[j]=1
        for x in p.keys():
            dp[i]=dp[i]|(dp[i-x*x]^True)
            # print(i,x,dp[i])


    # for i in range(1, n + 3):
    #     print(i, dp[i])

    return dp[n]


n = int(input())
print(winnerSquareGame(n))
