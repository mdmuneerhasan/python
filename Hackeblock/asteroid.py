from typing import List


def asteroidCollision(asteroids):
    ans = []

    for i in range(len(asteroids)):
        if len(ans) == 0:
            ans.append(asteroids[i])
        else:
            if ans[len(ans) - 1] <= 0 or asteroids[i] >= 0:
                ans.append(asteroids[i])
            else:
                while len(ans) > 0 and 0 < ans[len(ans) - 1] < abs(asteroids[i]):
                    ans.pop()
                if len(ans) == 0:
                    ans.append(asteroids[i])
                elif ans[len(ans) - 1] == abs(asteroids[i]):
                    ans.pop()
                    continue
                elif ans[len(ans) - 1] < -1*asteroids[i]:
                    ans.append(asteroids[i])

    return ans


x = [int(item) for item in input().split(' ')]
y = asteroidCollision(x)
print(y)
