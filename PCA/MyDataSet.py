class DataSet:
    def function(self, dimension, x):
        value = 0
        for i in range(len(dimension)):
            value += dimension[i] * (x ** (i + 1))
        return value

    def genrateDataset(self, endPoint, startPoint=0, points=100, error=0, random_state=11, degree=1):
        X = []
        Y = []
        dimensionValues = []
        for i in range(degree):
            if random_state == 0: random_state += 1
            x = (random_state ** 2 + i * i + 12 + 11 ** 2 + 3) % random_state
            if x == 0:
                random_state = (random_state ** 2 + i * i + 12 + 11 ** 2 + 3) % random_state
            dimensionValues.append(x)
            print(x)

        for i in range(points):
            if error == 0:
                e = 0
            else:
                e = ((((-1) ** i) * 2345 * i) / 100) % error
            x = startPoint + (endPoint - startPoint) * i / points
            Y.append(self.function(dimensionValues, x) + e + ((random_state * random_state) % endPoint))
            X.append(x)
        return X, Y
