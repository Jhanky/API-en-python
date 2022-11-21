from html import escape
from flask import Flask, make_response, jsonify, request
import controlador_actores
from datetime import date

app: Flask = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():  # put application's code here
    return '<h1> Esta es mi primera API en python </h1>' \
           '<hr>' \
           '<h3>Estos son los endpoints' \
           '<ul>' \
           '<li>Actores: <a href="/actores">http://127.0.0.1:5000/actores</a></li>'

@app.route('/insert', methods=["POST"])
def save_actor():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    last_update = request.form['last_update']
    controlador_actores.insert_actor(first_name, last_name, last_update)
    return 'actor guardado'

@app.route("/actores", methods=["GET"])
def actors():
    actores = controlador_actores.get_actors()
    return actores

@app.route("/actor/<id>", methods=["GET"])
def actor(id):
    actor = controlador_actores.get_actor_by_id(id)
    return actor

@app.route("/eliminar", methods=["POST"])
def delete_actor():
    controlador_actores.delete_actor_by_id(request.form['id'])
    return f'El actor con id = "{escape(request.form["id"])}" ha sido eliminado';

@app.route("/<name>", methods=["GET"])
def greeting(name):
    return f'Hola {escape(name)}, como estas?!'

@app.route('/actualizar', methods=["POST"])
def update_actor():

    first_name = request.form['name']
    last_name = request.form['lastname']
    actor_id = request.form['id']
    controlador_actores.update_actor(first_name, last_name, actor_id)
    return f'El actor con id = "{escape(request.form["id"])}" ha sido actualizado con exito';


if __name__ == '__main__':
    app.run()