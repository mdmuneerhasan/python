def solve(n):
    if n <= 1:
        return 0;
    if n % 2 == 0:
        return solve(n / 2)+1
    else:
        return min(solve(n - 1)+1,solve((n+1)/2)+2)


n = int(input())

print(solve(n))
