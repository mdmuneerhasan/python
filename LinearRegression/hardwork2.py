import matplotlib.pyplot as plt

X = [-30, -10, -1.5, 1, 2, 33, 4, 6, 8, 96, 4, 24, 6, 86, 4, 3, 50, 60, 70, 80]
Y = [-500, -100.3, -19.5, 25, 30, 498, 196, 91, 150, 1200, 100, 493, 93, 1293.5, 234, 48, 800, 803, 1053, 1203]

plt.scatter(X, Y, color='red')


def mean(values):
    return sum(values) / float(len(values))


def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar


def variance(values, mean):
    return sum([(x - mean) ** 2 for x in values])


def coefficients(x, y):
    # x = [row[0] for row in dataset]
    # y = [row[1] for row in dataset]
    x_mean, y_mean = mean(x), mean(y)
    b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    b0 = y_mean - b1 * x_mean
    return [b0, b1]


def predict(b0, b1, X):
    Y = []
    for i in range(len(X)):
        Y.append(b0 + b1 * X[i])
        print("when x = " + str(X[i]) + " y = " + str(Y[i]))
    return Y


b0, b1 = coefficients(X, Y)
print('Linear regression equation y = %.2f + %.2f * x' % (b0, b1))

X = [-200, 200,0]

Y = predict(b0, b1, X)

plt.plot(X, Y,color='blue')
plt.savefig('graph2')
