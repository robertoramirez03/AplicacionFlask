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

@rutas_usuarios.route('/formulario_supervivientes', methods=['POST'])
def formulario_supervivientes():
    nombre_jugador = request.form['nombre_jugador'] 
    superviviente_favorito = request.form['superviviente_favorito'] 
    color_de_pelo = request.form['color_de_pelo']
    complexion = request.form['complexion']

    cursor = db.database.cursor()  
    sql = "INSERT INTO Supervivientes (Nombre,Apellido,CentroFormativo) VALUES (%s, %s, %s,%s)" 
    data = (nombre_jugador,superviviente_favorito,color_de_pelo,complexion) 
    cursor.execute(sql,data) 
    db.database.commit() 

