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
    try:
        f = open("datos.txt", 'r')
    except OSError:
        # Devolver error en caso de que no se pueda leer el archivo
        return jsonify({'success': False, 'message' : "Error a la hora de leer"})

    # leer datos
    mensaje = f.read()
    # cerrar fichero
    f.close()
    # Devolver json con los datos
    return jsonify({'success': True, 'message' : mensaje})

@app.route("/guardar", methods = ['POST'])
def write_to_file():
    # Suponer que llega una request con el siguiente json
    request = ({'file': "datos.txt", 'message' : "Mensaje para ser escrito en el fichero"})
    
    try:
        f = open(request['file'], "a")
    except OSError:
        #  Devolver error en el caso de que el post no funcione
        return jsonify({'success': False, 'message' : "Error a la hora de escribir"})

    f.write(request['message'])
    f.close()
    # Devolver json con el mensaje 
    return jsonify({'success': True, 'message':"Se ha escrito correctamente"})