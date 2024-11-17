from multiprocessing.managers import Value
from sys import excepthook

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                error = "Las notas deben estar entre 10 y 70."
                return render_template('ejercicio1.html', error=error)

            if not (0 <= asistencia <= 100):
                error = "La asistencia debe estar entre 0% y 100%."
                return render_template('ejercicio1.html', error=error)

            promedio = (nota1 + nota2 + nota3) / 3
            estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"

            return render_template('ejercicio1.html', promedio=promedio, estado=estado)

        except ValueError:
            error = "Por favor, ingrese valores numéricos válidos."
            return render_template('ejercicio1.html', error=error)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET','POST'])
def ejercicio2():
    if request.method == 'POST':
        try:
            nombre1 = str(request.form['nombre1'])
            nombre2 = str(request.form['nombre2'])
            nombre3 = str(request.form['nombre3'])

            if len(set([nombre1, nombre2, nombre3])) < 3:
                error = "Los nombres deben ser diferentes."
                return render_template('ejercicio2.html', error=error)

            nombres = [nombre1, nombre2, nombre3]
            nombre_mayor = max(nombres, key=len)
            cantidad_caracteres = len(nombre_mayor)

            # Retornamos el resultado al template
            return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, cantidad_caracteres=cantidad_caracteres)

        except Exception as e:
            error = f"Ocurrió un error: {str(e)}"
            return render_template('ejercicio2.html', error=error)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)