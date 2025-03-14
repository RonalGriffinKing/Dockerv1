from flask import Flask,request,jsonify,render_template

from pymongo import MongoClient

import os

app=Flask(__name__)
MONGO_URI=os.getenv('MONGO_URI','mongodb://localhost:27017')
client=MongoClient(MONGO_URI)
db=client['daw_exam']
collection=db['objetos']

@app.route("/",methods=['GET'])
def index():
    objetos= list(collection.find({},{'_id':0}))
    return render_template('index.html',messaje=objetos)

    

@app.route("/objetos",methods=['POST'])
def crear_objeto():
    nombre=request.form.get("nombre")
    edad=request.form.get("edad")
    correo=request.form.get("correo")
    signo=request.form.get("signo")
    objeto={
        'Nombre':nombre,'Edad':edad, 'Correo':correo,'Signo':signo
    }
    if nombre and edad and correo and signo:
        collection.insert_one(objeto)
        return jsonify({'Mensaje':'Ingresado con exito'})
    return jsonify({'Mensaje':'Te falto agregar un dato'})
    
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)