from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)

from Controladores.ControladorUsuario import ControladorUsuario
miControladorUsuario=ControladorUsuario()

@app.route("/",methods=['GET'])
def test():
    json={}
    json["message"]="Server running ..."
    return jsonify(json)

@app.route("/usuarios",methods=['GET'])
def getUsuarios():
    json=miControladorUsuario.index()
    return jsonify(json)

@app.route("/usuarios",methods=['POST'])
def crearUsuario():
    data = request.get_json()
    json=miControladorUsuario.create(data)
    return jsonify(json)

@app.route("/usuarios/<string:id>",methods=['GET'])
def getUsuario(id):
    json=miControladorUsuario.show(id)
    return jsonify(json)

@app.route("/usuarios/<string:id>",methods=['PUT'])
def modificarUsuario(id):
    data= request.get_json()
    json=miControladorUsuario.update(id,data)
    return jsonify(json)

@app.route("/usuarios/<string:id>",methods=['Delete'])
def eliminarUsuariuo(id):
    json=miControladorUsuario.delete(id)
    return jsonify(json)

def loadFileConfig():
  with open('config.json') as f:
    data = json.load(f)
  return data

if __name__=='__main__':
  dataConfig = loadFileConfig()
  print("Server running : "+"http://"+dataConfig["url-backend"]+":"+ str(dataConfig["port"]))
  serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])