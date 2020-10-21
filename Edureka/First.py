import sys
import matplotlib.pyplot as plt
import numpy
import pandas
import plot
import scipy
import sklearn
from pandas.plotting import scatter_matrix
from sklearn import model_selection

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
print(dataset.shape)
print(dataset.head(30))
print(dataset.describe())
print(dataset.groupby('class').size())
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=True, sharey=True)
dataset.hist()
scatter_matrix(dataset)
plt.savefig("mygraph.png")

array = dataset.values
print(array)
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 6
X_train, x_test, Y_train, y_test = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
scoring = 'accuracy'


