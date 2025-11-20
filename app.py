# app.py
from flask import Flask
from flask import render_template
from flask import request

# Crear la aplicación Flask con el nombre del módulo actual que se está ejecutando contemplando la estructura de carpetas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')