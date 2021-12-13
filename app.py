from flask import Flask,render_template,request
import pandas as pd 
from Superdataframe import Superdataframe
from sacarCopia import mainCopia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main',methods=['POST'])
def main():
    if request.method == 'POST':
        try:
            pais = request.form['pais']
        except KeyError:
            pais = 'Colombia' 
        
        r = mainCopia()
        
        if r == 'NoCopiados':
            print('Registros No Copiados')
        elif r == 'RegistrosCopiados':
            print('Registros Copiados')
            
        df = pd.read_csv("df/df.csv",delimiter=',')   
        reportePais = Superdataframe(pais,df)

        dfCasos          = reportePais.topPaises('cases')
        dfMuertes        = reportePais.topPaises('deaths')
        dataframe        = reportePais.dataframe()

        topCasos = dfCasos[dfCasos['pais'] == pais]
        topMuertes = dfMuertes[dfMuertes['pais'] == pais]

        try:
            topCasosArriba = dfCasos[dfCasos['top'] == (topCasos['top'].tolist()[0]-1)].loc[:, ['pais','frecuencia']]
        except Exception as e:
            topCasosArriba = 0
        
        try:    
            topCasosAbajo = dfCasos[dfCasos['top'] == (topCasos['top'].tolist()[0]+1)].loc[:, ['pais','frecuencia']]
        except Exception as e:
            topCasosAbajo = 0

        try:
            topMuertesArriba = dfMuertes[dfMuertes['top'] == (topMuertes['top'].tolist()[0]-1)].loc[:, ['pais','frecuencia']]
        except Exception as e:
            topMuertesArriba = 0

        try:
            topMuertesAbajo = dfMuertes[dfMuertes['top'] == (topMuertes['top'].tolist()[0]+1)].loc[:, ['pais','frecuencia']]
        except Exception as e:
            topMuertesAbajo = 0
        
        try:
            fechaMaxCasos   = dataframe[(dataframe['casos'].isin([max(dataframe['casos'])]) )].loc[: ,['fecha','casos']]
        except Exception as e:
            fechaMaxCasos = 'NA'
        
        try:
            fechaMaxMuertes = dataframe[(dataframe['muertes'].isin([max(dataframe['muertes'])]) )].loc[: ,['fecha','muertes']]
        except Exception as e:
            fechaMaxMuertes = 'NA'
            

        data = {
                'reporte'            : dataframe,
                'fecha'              : reportePais.fechaMax(),
                'casosHoy'           : reportePais.casosConfirmadoshoy(),
                'fallecidosHoy'      : reportePais.fallecidoshoy(),
                'casos'              : reportePais.casosConfirmados(),
                'fallecidos'         : reportePais.fallecidos(),
                'casosCurva'         : reportePais.casosCurva()[0],
                'vec_fecha'          : reportePais.casosCurva()[1],
                'casosDiarios'       : reportePais.casosDiarios(),
                'muertesCurva'       : reportePais.muertesCurva(),
                'muertesDiarios'     : reportePais.muertesDiarios(),
                'topPaises'          : dfCasos,
                'pais'               : reportePais.selectPais(),
                'top'                : topCasos,
                'topMuertes'         : topMuertes,
                'topCasosArriba'     : topCasosArriba,
                'topCasosAbajo'      : topCasosAbajo,
                'topMuertesArriba'   : topMuertesArriba,
                'topMuertesAbajo'    : topMuertesAbajo,
                'fechaMaxCasos'      : fechaMaxCasos,
                'fechaMaxMuertes'    : fechaMaxMuertes
               } 
        return render_template('main.html',data=data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)