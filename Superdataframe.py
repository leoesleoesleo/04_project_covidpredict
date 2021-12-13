import pandas as pd 
from datetime import datetime, timedelta

class Superdataframe:
    def __init__(self,pais,df):
        self.df   = df
        self.res  = self.df[(self.df['countriesAndTerritories'].isin([pais]) )]
        self.pais = pais
        
    def selectPais(self):
        return self.pais
    
    def extremosFecha(self):
        v_fecha = []
        for i in range(len(self.res)):
            fecha = datetime.strptime(self.res.iloc[i,0], '%d/%m/%Y')
            v_fecha.append(fecha)
        return min(v_fecha),max(v_fecha)    

    def dataframe(self):
        fechaMin         = self.extremosFecha()[0]
        fechaMax         = self.extremosFecha()[1]
        auxFecha         = fechaMin
        auxCasos         = 0
        auxMuertes      = 0   
        v_mes_dia     = []
        v_fecha       = []
        v_fechaformat = []
        v_casos       = []
        c_casosAcum   = []
        c_muertes     = []
        v_muertesAcum = []    
        
        while auxFecha < fechaMax:
            v_fecha.append(str(auxFecha)[0:10])
            v_fechaformat.append(auxFecha)
            v_mes_dia.append(str(auxFecha)[5:10])
            try:
                casos = self.res[(self.res['day'].isin([str(auxFecha)[8:10]]) & self.res['month'].isin([str(auxFecha)[5:7]]) & self.res['year'].isin([str(auxFecha)[0:4]]) )]['cases'].tolist()[0]
            except Exception as e:
                casos = 0        
            try:
                muertes = self.res[(self.res['day'].isin([str(auxFecha)[8:10]]) & self.res['month'].isin([str(auxFecha)[5:7]]) & self.res['year'].isin([str(auxFecha)[0:4]]) )]['deaths'].tolist()[0]
            except Exception as e:
                muertes = 0            
            v_casos.append(casos)
            c_casosAcum.append(auxCasos+casos)  
            c_muertes.append(muertes)
            v_muertesAcum.append(auxMuertes+muertes)
            auxCasos   += casos
            auxMuertes += muertes 
            auxFecha   += timedelta(days=1)
               
        d = {
             'fecha'        : v_fecha, 
             'fechaformato' : v_fechaformat, 
             'dia_mes'      : v_mes_dia,
             'casos'        : v_casos,
             'casosAcum'    : c_casosAcum,
             'muertes'      : c_muertes,
             'muertesAcum'  : v_muertesAcum
             }    
        return pd.DataFrame(data=d)
    
    def sumCasos(self):
        return self.df ['cases'].sum()
    
    def maxCasos(self):
        return max(self.df ['cases'])
        
    def fechaMax(self):
        df = self.dataframe()
        df = max(df['fecha'])
        return df
    
    def casosConfirmadoshoy(self):
        df = self.dataframe()
        df = df[(df['fechaformato'].isin([max(df['fechaformato'])]) )]['casos'].tolist()[0]
        return df
    
    def fallecidoshoy(self):
        df = self.dataframe()
        df = df[(df['fechaformato'].isin([max(df['fechaformato'])]) )]['muertes'].tolist()[0]
        return df
   
    def casosConfirmados(self):
        df = self.dataframe()
        df = df[(df['fechaformato'].isin([max(df['fechaformato'])]) )]['casosAcum'].tolist()[0]
        return df
    
    def fallecidos(self):
        df = self.dataframe()
        df = df[(df['fechaformato'].isin([max(df['fechaformato'])]) )]['muertesAcum'].tolist()[0]
        return df
    
    def casosCurva(self):
        df = self.dataframe()
        dfcasos = df['casosAcum'].tolist()
        dfecha  = df['dia_mes'].tolist()
        return dfcasos,dfecha
    
    def casosDiarios(self):
        df = self.dataframe()
        df = df['casos'].tolist()
        return df
    
    def muertesCurva(self):
        df = self.dataframe()
        df = df['muertesAcum'].tolist()
        return df
    
    def muertesDiarios(self):
        df = self.dataframe()
        df = df['muertes'].tolist()
        return df
    
    def topPaises(self,param):
        df = self.df 
        df = df.groupby(['countriesAndTerritories'])[param].sum().sort_values(ascending=False)
        vec_pais       = []
        vec_frecuencia = []
        vec_top        = []
        vec_porcentaje = []
        c = 1
        max_ = 0
        for i in range(100):
            vec_pais.append(df.index.values[i])
            vec_frecuencia.append(df[i]) 
            if max_ < df[i]:
                max_ = df[i]
            vec_porcentaje.append((df[i]/max_)*100) 
            vec_top.append(c)
            c += 1
        d = {
             'top'         : vec_top, 
             'pais'        : vec_pais, 
             'frecuencia'  : vec_frecuencia,
             'porcentaje'  : vec_porcentaje
             }    
        df = pd.DataFrame(data=d)  
        return df

"""
pais = 'Colombia' 
#df = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/casedistribution/csv",delimiter=',')   
df = pd.read_csv("df/df.csv",delimiter=',')
reportePais = Superdataframe(pais,df)

dataframe     = reportePais.dataframe()

reportePais.selectPais()
#reportePais.maxCasos()
#reportePais.sumCasos()

reportePais.topPaises('cases')

fechaMaxCasos   = dataframe[(dataframe['casos'].isin([max(dataframe['casos'])]) )].loc[: ,['fecha','casos']]
fechaMaxMuertes = dataframe[(dataframe['muertes'].isin([max(dataframe['muertes'])]) )].loc[: ,['fecha','muertes']]

dfCasos = reportePais.topPaises('cases')
dfMuertes = reportePais.topPaises('deaths')

dfCasos          = reportePais.topPaises('cases')
dfMuertes        = reportePais.topPaises('deaths')

topCasos = dfCasos[dfCasos['pais'] == pais]
topMuertes = dfCasos[dfCasos['pais'] == pais]

topCasosArriba = dfCasos[dfCasos['top'] == (topCasos['top'].tolist()[0]-1)].loc[:, ['pais','frecuencia']]
topCasosAbajo = dfCasos[dfCasos['top'] == (topCasos['top'].tolist()[0]+1)].loc[:, ['pais','frecuencia']]

topMuertesArriba = dfMuertes[dfMuertes['top'] == (topMuertes['top'].tolist()[0]-1)].loc[:, ['pais','frecuencia']]
topMuertesAbajo = dfMuertes[dfMuertes['top'] == (topMuertes['top'].tolist()[0]+1)].loc[:, ['pais','frecuencia']]

#dataframe.to_csv('df/prueba2.csv', header=True, index=False)
"""

    
    
