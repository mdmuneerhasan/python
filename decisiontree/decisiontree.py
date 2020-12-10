import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("train.csv")
columns_to_drop = ["PassengerId", "Name", "Ticket", "Cabin", "Embarked"]
data_clean = data.drop(columns_to_drop, axis=1)

data_clean["Sex"] = LabelEncoder().fit_transform(data_clean["Sex"])

data_clean = data_clean.fillna(data_clean["Age"].mean())

input_cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
output_cols = ['Survived']
X = data_clean[input_cols]
Y = data_clean[output_cols]

def entropy(col):
    count=np.unique(col,return_counts=True)
    N=float(col.shape[0])
    ent=0.0
    for ix in count[1]:
        p=ix/N
        ent+=(-1.0*p*np.log2(p))
    return ent


def divide_data(x_data, fkey, fval):
    x_right=pd.DataFrame([],columns=x_data.columns)
    x_left=pd.DataFrame([],columns=x_data.columns)
    for ix in range(x_data.shape[0]):
        val=x_data[fkey].loc[ix]
        if val>fval:
            x_right=x_right.append(x_data.loc[ix])
        else:
            x_left=x_left.append(x_data.loc[ix])
    return x_left,x_right


def information_gain(x_data,fkey,fval):
    left,right=divide_data(x_data,fkey,fval)
    l=float(left.shape[0])/x_data.shape[0]
    r=float(right.shape[0])/x_data.shape[0]
    if left.shape[0]==0 or right.shape[0] == 0:
        return -10000000
    i_gain=entropy(x_data.Survived)-(l*entropy(left.Survived))-(r*entropy(right.Survived))
    return i_gain


class DecisionTree:

    def __init__(self, depth=0, max_depth=5):
        self.left = None
        self.right = None
        self.fkey = None
        self.fval = None
        self.max_depth = max_depth
        self.depth = depth
        self.target = None


    def train(self,X_train):
        features=['Pclass','Sex','Age','SibSp','Parch','Fare']
        info_gains=[]
        for ix in features:
            i_gain=information_gain(X_train,ix,X_train[ix].mean())
            info_gains.append(i_gain)
        self.fkey=features[np.argmax(info_gains)]
        self.fval=X_train[self.fkey].mean()

        print("Making Tree Features is ",self.fkey)

        data_left,data_right=divide_data(X_train,self.fkey,self.fval)
        data_left=data_left.reset_index(drop=True)
        data_right=data_right.reset_index(drop=True)
        if data_left.shape[0] == 0 or data_right.shape[0]==0:
            if X_train.Survived.mean() >= 0.5:
                self.target="Survive"
            else:
                self.target="Dead"
            return

        if self.depth>=self.max_depth:
            if X_train.Survived.mean() >= 0.5:
                self.target="Survive"
            else:
                self.target="Dead"
            return
        self.left=DecisionTree(depth=self.depth+1,max_depth=self.max_depth)
        self.left.train(data_left)

        self.right=DecisionTree(depth=self.depth+1,max_depth=self.max_depth)
        self.right.train(data_right)

        if X_train.Survived.mean() >= 0.5:
            self.target="Survive"
        else:
            self.target="Dead"
        return

    def predict(self,test):
        if test[self.fkey]>self.fval:
            if self.right is None:
                return self.target
            return self.right.predict(test)
        else:
            if self.right is None:
                return self.target
            return self.left.predict(test)



split=int(.7*data.shape[0])
training_data=data_clean[:split]
test_data=data_clean[split:]
test_data=test_data.reset_index(drop=True)
dt=DecisionTree()
dt.train(training_data)

# print(dt.fkey)
# print(dt.fval)
# print(dt.left.fkey)
# print(dt.right.fkey)

y_pred=[]
y_actual=test_data[output_cols]

for ix in range(test_data.shape[0]):
    y_pred.append(dt.predict(test_data.loc[ix]))

y_pred=LabelEncoder().fit_transform(y_pred)


y_pred=np.array(y_pred).reshape((-1,1))

acc=np.sum(np.array(y_pred)==np.array(y_actual))/y_pred.shape[0]

print(acc)