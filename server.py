from flask import Flask
from flask import jsonify

app = Flask(__name__)

# Main page
@app.route("/")
def hello_world():
    return "<p>Main page</p>"


# Metodo get que devuelve datos harcodeados como json
@app.route("/datos", methods = ['GET'])
def return_hardcoded_json():
    # Abrir fichero en modo lectura
    f = open("datos.txt", 'r')
    # leer datos
    mensaje = f.read()
    # cerrar fichero
    f.close()
    # Devolver json con los datos
    return jsonify({'success': True, 'message' : mensaje})

 