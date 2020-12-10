def bagOfTokensScore(tokens, P):
    tokens = list(tokens)
    tokens.sort()
    ans = 0
    j = len(tokens) - 1
    i = 0
    while i <j and P >= tokens[i]:
        while i <= j and P >= tokens[i]:
            ans += 1
            P -= tokens[i]
            i += 1
        if i < j and ans > 0:
            ans -= 1
            P += tokens[j]
            j -= 1
    if i <= j and P >= tokens[i]:
        ans += 1
        P -= tokens[i]
        i += 1

    return ans


t = map(int, input().split(','))
p = int(input())
print(bagOfTokensScore(t, p))

100, 200
500

58,91
50