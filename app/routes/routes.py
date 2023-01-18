from flask import Blueprint, render_template, request

from app import db
#from app.data.equipo_dao import EquipoDao
rutas_usuarios = Blueprint("routes", __name__)

@rutas_usuarios.route("/")
def index():
    return render_template("index.html")

@rutas_usuarios.route("/supervivientes")
def supervivientes():
    return render_template("supervivientes.html")

@rutas_usuarios.route("/asesinos")
def asesinos():
    return render_template("asesinos.html")