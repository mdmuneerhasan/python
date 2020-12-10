import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("train.csv")
columns_to_drop = ["PassengerId", "Name", "Ticket", "Cabin", "Embarked"]
data_clean = data.drop(columns_to_drop, axis=1)

data_clean["Sex"] = LabelEncoder().fit_transform(data_clean["Sex"])

data_clean = data_clean.fillna(data_clean["Age"].mean())

input_cols = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
output_cols = ['Survived']
X = data_clean[input_cols]
Y = data_clean[output_cols]

split=int(.7*data.shape[0])
train_data=data_clean[:split]
test_data=data_clean[split:]
test_data=test_data.reset_index(drop=True)


sk_tree=DecisionTreeClassifier(criterion='entropy',max_depth=5)
sk_tree.fit(train_data[input_cols],train_data[output_cols])
a=sk_tree.predict(test_data[input_cols])

print(a)

acc=sk_tree.score(test_data[input_cols],test_data[output_cols])

print(acc)