# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:43:36 2020

@author: leonardo.patino
"""
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


df = pd.read_csv("df.txt",delimiter=',')

diasAtras = 7
v_casosMovil = []
for i in range(len(df)):
    if i >= diasAtras:
        v_casosMovil.append(sum(df['casos'][(i-diasAtras):(i-1)]))
    else:
        v_casosMovil.append(0)

df['casosMovil'] = v_casosMovil
df['num'] = df.index


X_train = df.loc[:,['casos','muertesAcum','casosMovil','num']]
y_train = df['casosAcum']

model = DecisionTreeClassifier()    
model.fit(X_train, y_train)

model.predict(X_test)
score = model.score(X_train, y_train)


                    

      