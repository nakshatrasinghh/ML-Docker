#@ Necessay dependancies and libraries required
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#@ Parsing csv file using pandas 
df = pd.read_csv('mobile.csv')

#@ Setting our variables for training from our dataFrame into numpy arrays
y_t = np.array(df['price_range']) 
x_t = df
x_t = df.drop(['price_range'], axis=1)
x_t = np.array(x_t)

#@ Scaling down the non-target numpy variable using min-max scaler 
scaler = MinMaxScaler() 
x_t = scaler.fit_transform(x_t)

#@ Performing train test split
X_train, X_test, Y_train, Y_test = train_test_split(x_t, y_t, test_size=.20)

#@ Decision tree classifer with differnt max_depth and gini impurity 
dtc = DecisionTreeClassifier(max_depth=7, criterion='gini', max_features=20, min_samples_split=4)
dtc.fit(X_train, Y_train) 
scoretrain = dtc.score(X_train, Y_train)
scoretest = dtc.score(X_test, Y_test) 
print(f"Training score: {scoretrain}, Tesing score: {scoretest}") 
