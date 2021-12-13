
#
# Dashboard Covid
Por: Leonardo Patiño Rodriguez
<div align="center">
	<img height="200" src="https://leoesleoesleo.github.io/imagenes/flask_bootstrap.png" alt="PokeAPI">
</div>  

## &nbsp; [![pyVersion37](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/download/releases/3.7/)

# Manual de instalación

### Características
<p align="justify">
Características habituales proporcionadas por Flask:
Este es un marco de micro web escrito en Python. Se clasifica como un microframework porque no requiere herramientas o bibliotecas particulares. No tiene una capa de abstracción de base de datos, validación de formularios ni ningún otro componente donde las bibliotecas de terceros preexistentes brinden funciones comunes.
</p>
<p align="justify">
Bootstrap es un marco CSS gratuito y de código abierto dirigido al desarrollo web front-end receptivo y móvil. Contiene plantillas de diseño basadas en CSS y JavaScript para tipografía, formularios, botones, navegación y otros componentes de la interfaz.
</p>

### Pasos

- Clonar repositorio
  ```
  git clone https://github.com/leoesleoesleo/04_project_covidpredict.git
  ```
- Crear entorno virtual

    Ejemplo anaconda
   ```
   conda create -n coviDashboard python=3.7.9 
   ```
   ```
   conda activate coviDashboard
   ```

- Navegar hasta la carpeta del proyecto para instalar dependencias
    ```
    pip install -r requirements.txt
    ```

- Iniciar programa
    ```
    python app.py
    ```
    ```sh
    127.0.0.1:5000
    ```
#### Ejemplo
<div>
	<img height="400" width="800" src="https://leoesleoesleo.github.io/imagenes/covidpredict.png" alt="PokeAPI">
</div>  
<div>
	<img height="400" width="800" src="https://leoesleoesleo.github.io/imagenes/covidpredict2.png" alt="PokeAPI">
</div> 
<div>
	<img height="400" width="800" src="https://leoesleoesleo.github.io/imagenes/covidpredict3.png" alt="PokeAPI">
  <img height="400" width="800" src="https://leoesleoesleo.github.io/imagenes/covidpredict4.png" alt="PokeAPI">
</div> 

##
## MANUAL TÉCNICO

### Contexto

<p align="justify">
  Exponer un dashboard con la información básica de las muertes e infectados del covid, este consume un servicio que contiene los datos, los procesa y los pinta en graficas y tablas.
</p>

## Fuentes de datos

Se consume el siguientes servicios:  
```
https://opendata.ecdc.europa.eu/covid19/casedistribution/csv
```
