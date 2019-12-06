# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:39:23 2019

@author: Jehanzeb Babar
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
9
dataset = pd.read_csv("aids.csv")
X = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,2].values 

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y , test_size = 0.2 ,random_state = 0)

from sklearn.linear_model import LinearRegression 
regressor  = LinearRegression()
regressor.fit(X_train,y_train)
regressor.predict(X_test)

while True:
   n = int(input("enter a number between 1980 and 2000: "))
   if (n < 2001) & (n > 1979) :
      break
   print('please enter the correct value')
   


plt.scatter(X_train , y_train , color="red") # training set line 
plt.plot(X_train, regressor.predict(X_train), color = "blue") # predicted values
plt.title("YEARS VS DEATHS BY AIDS")
plt.xlabel("years")
plt.ylabel("deaths")
plt.show()

plt.scatter(X_test , y_test , color="red") # testing set line 
plt.plot(X_train, regressor.predict(X_train), color = "blue") # predicted values
plt.title("YEARS VS DEATHS BY AIDS")
plt.xlabel("years")
plt.ylabel("deaths")
plt.show()

print("Year =",n)

print("Average deaths per years are given below")
print(regressor.predict([[n]]))







