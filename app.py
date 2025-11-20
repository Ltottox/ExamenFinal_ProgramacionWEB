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
    resultado = None
    precio_tarro = 9000

    if request.method == 'POST': 
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        cantidad_tarro = int(request.form.get("cantidad_tarro"))
        
        #calculo del precio total sin descuento
        precio_tarro_sin_descuento = precio_tarro * cantidad_tarro
        #descuento segun edad
        descuento = 0
        if 18 <= edad <= 30: descuento = 0.15
        elif edad > 30: descuento = 0.25
        

        #calculo del precio con descuento
        precio_con_descuento = precio_tarro_sin_descuento * descuento
        total_a_pagar = precio_tarro_sin_descuento - precio_con_descuento

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": precio_tarro_sin_descuento,
            "precio_con_descuento": round(precio_con_descuento),
            "total_a_pagar": round(total_a_pagar)
        }
        
        return render_template('ejercicio1.html', resultado=resultado)
    return render_template('ejercicio1.html')

    

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()