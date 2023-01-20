from flask import Blueprint, render_template, request

from app import db
rutas_usuarios = Blueprint("routes", __name__)

@rutas_usuarios.route("/")
def index():
    return render_template("index.html")

@rutas_usuarios.route("/formulario")
def formulario():
    return render_template("formulario.html")

@rutas_usuarios.route("/datos")
def datos():
    return render_template("datos.html")




@rutas_usuarios.route('/formulario_supervivientes', methods=['POST'])
def formulario_supervivientes():
    nombre_jugador = request.form['nombre_jugador'] 
    superviviente_favorito = request.form['superviviente_favorito'] 
    asesino_favorito = request.form['asesino_favorito']

    if (nombre_jugador and superviviente_favorito and asesino_favorito):
        cursor = db.database.cursor()  
        sql = "INSERT INTO Jugadores (Nombre_Jugador,Superviviente_Favorito,Asesino_Favorito) VALUES (%s, %s, %s)" 
        data = (nombre_jugador,superviviente_favorito,asesino_favorito) 
        cursor.execute(sql,data) 
        db.database.commit() 
    
    

