import numpy as np
import matplotlib.pyplot as plt

X = np.arange(10)
Y = (X - 5) ** 2
print(X, Y)
plt.style.use("seaborn")
plt.plot(X, Y)
plt.ylabel("F(X)")
plt.xlabel("X")

x = 0
lr = 0.1
error = []
for i in range(50):
    grad = 2 * (x - 5)
    x = x - lr * grad
    y = (x - 5) ** 2
    error.append(y)
    plt.scatter(x, y)

    print(x)

plt.savefig("123")
plt.clf()
plt.plot(error)
plt.savefig("error")