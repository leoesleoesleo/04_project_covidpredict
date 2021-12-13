# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:56:06 2020

@author: leonardo.patino
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split 

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.neural_network import MLPRegressor

def test(y_test,X_test):
    confianza = 20
    itera = len(y_test)
    y_traget = []
    y_testt = []
    win = []
    loose = []
    
    i = 0
    while i < itera:
        X_test_ = X_test.iloc[i]
        predict = model.predict([X_test_])[0]
        y_test_ = y_test.iloc[i] 
        
        if predict in range((y_test_-confianza),(y_test_+confianza)):
            r="win"
            win.append(1)        
        else:
            r="loose"  
            loose.append(1)
        
        y_traget.append(predict) # no/si
        y_testt.append(y_test_)    
         
        i = i + 1    
        
        print("Predicción: ",predict," Se esperaba: ",y_test_, "Resultado: ",r) 
   
    print("ganadas ",len(win))
    print("perdidas ",len(loose))
    print("Score: ",score)
    print("Ganadas vs Perdidas: %",(len(win)*100/(len(win)+len(loose))))


df = pd.read_csv("df/prueba.csv",delimiter=';')
df.dropna(inplace=True)

X = df.loc[:,['x2','max_f','media_f','de_f']]
#X = Normalizer().fit(X)

y = df['casos']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)  

"""
X_test = df.loc[109:,['x2','max_f','media_f','de_f','Num']]
X_train = df.loc[0:108,['x2','max_f','media_f','de_f','Num']]
y_test = df.loc[109,['casosAcum']]
y_train = df.loc[0:108,['casosAcum']]
"""

"""
plt.scatter(X,y)
plt.title('Tendecia')
plt.show()
"""

model = DecisionTreeClassifier()    
#model = linear_model.LinearRegression()
#model  = MLPRegressor(activation='logistic', hidden_layer_sizes=(100,100,100,100), random_state=1, max_iter=500, max_fun=15000)
#model  = MLPRegressor(hidden_layer_sizes=(10,50,50,10), random_state=1, max_iter=500)
#model.fit(X_train, y_train)
model.fit(X_train, y_train)
score = model.score(X_train, y_train)
print(score)
#model.predict(X_test)

#y_pred = model.predict(X_test)

test(y_test,X_test)


"""
plt.scatter(X_test,y_test)
plt.plot(X_test,y_pred, color='red', linewidth=3)
plt.title('Red Neuronal')
plt.show()
"""


#TESTEAT
"""
df = pd.read_csv("df/prueba2.csv",delimiter=';')
df.dropna(inplace=True)

X_test = df.loc[:,['x2','max_f','media_f','de_f']]
y_test = df['casos']  

test(y_test,X_test)
"""









