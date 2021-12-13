# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:29:48 2020

@author: leonardo.patino
"""
import pandas as pd
from datetime import date,datetime

def copia():
    df = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv",delimiter=',')   
    df.to_csv('df/df.csv', header=True, index=False)
    file = open ('conf/val.txt','w')
    file.write(str(date.today()))
    file.close()
    return "RegistrosCopiados"

def mainCopia():
    archivo = open('conf/val.txt', 'r')
    for i in archivo.readlines():
        var = i
        archivo.close() 

    diferencia = datetime.strptime(str(date.today()), '%Y-%m-%d') - datetime.strptime(var, '%Y-%m-%d')
    if diferencia.days >= 1:
        res = copia()
    else:
        res = "NoCopiados"
    return res
    

