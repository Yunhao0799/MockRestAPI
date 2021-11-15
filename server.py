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
    return jsonify({'success': True, 'message' : "Este es un mensaje harcodeado del metodo get"})

