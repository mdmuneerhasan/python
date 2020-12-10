import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = pd.read_csv("Linear_X_Train.csv")
Y = pd.read_csv("Linear_Y_Train.csv")


# converting X ,Y to numpy
X = X.values
Y = Y.values

print(X)
print(Y)
# normalisation
u = X.mean()
std = X.std()
X = (X - u) / std

# Visualize
plt.scatter(X, Y, color='orange')
plt.style.use("seaborn")


# plt.savefig("graph")


def hypothesis(x, theta):
    # theta
    y_ = theta[0] + theta[1] * x
    return y_


def gradient(X, Y, theta):
    m = X.shape[0]
    grad = np.zeros((2,))
    for i in range(m):
        x = X[i]
        y_ = hypothesis(x, theta)
        y = Y[i]
        grad[0] += (y_ - y)
        grad[1] += (y_ - y) * x
    return grad / m


def error(X, Y, theta):
    m = X.shape[0]
    total_error = 0.0
    for i in range(m):
        y_ = hypothesis(X[i], theta)
        total_error += (y_ - Y[i]) ** 2
    return total_error / m


def gradientDescent(X, Y, max_steps=100, learning_rate=0.1):
    theta = np.zeros((2,))
    error_list = []
    for i in range(max_steps):
        grad = gradient(X, Y, theta)
        e = error(X, Y, theta)
        error_list.append(e)
        theta[0] = theta[0] - learning_rate * grad[0]
        theta[1] = theta[1] - learning_rate * grad[1]

    return theta, error_list


theta, error_list = gradientDescent(X, Y)
print(theta)
plt.clf()
plt.plot(error_list)
# plt.savefig("graph2")

y_ = hypothesis(X, theta)

plt.clf()
plt.scatter(X, Y)
plt.plot(X, y_, color='orange', label='prediction')
plt.legend()
# plt.savefig("graph3")

X_test = pd.read_csv('sample_submission_linear.csv').values

y_test = hypothesis(X_test, theta)
df = pd.DataFrame(data=y_test, columns=["y"])
df.to_csv('y_prediction.csv', index=False)

plt.clf()
plt.scatter(X_test, y_test, color='black')
plt.savefig("graph4")
