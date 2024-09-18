from flask import Flask

from flask import render_template
from flask import request

import pusher

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("app.html")

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/alumnos/guardar", methods=["POST"])
def alumnosGuardar():
    matricula      = request.form["txtMatriculaFA"]
    nombreapellido = request.form["txtNombreApellidoFA"]
    return f"Matrícula {matricula} Nombre y Apellido {nombreapellido}"

def evento():
    pusher_client = pusher.Pusher(
        app_id = "1766031",
        key = "75c20f55afe54f98e3ce",
        secret = "29cf7167529f0d20916a",
        cluster = "us2",
        ssl=True
    )
    
    pusher_client.trigger("my-channel", "my-event", {})
