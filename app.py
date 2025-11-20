# app.py
from flask import Flask
from flask import render_template
from flask import request

# Crear la aplicación Flask con el nombre del módulo actual que se está ejecutando contemplando la estructura de carpetas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()