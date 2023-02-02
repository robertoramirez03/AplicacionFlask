from flask import Blueprint, render_template, request,  redirect, url_for
from app.data.supervivientes_dao import Jugadores_dao

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
    jugadores_dao = Jugadores_dao()
    jugadores = jugadores_dao.select_all(db)
    return render_template("datos.html", jugadores=jugadores)





@rutas_usuarios.route('/formulario_jugador', methods=['POST'])
def formulario_jugador():
    nombre_jugador = request.form['nombre_jugador'] 
    superviviente_favorito = request.form['superviviente_favorito'] 
    asesino_favorito = request.form['asesino_favorito']

    if (nombre_jugador and superviviente_favorito and asesino_favorito):
        cursor = db.cursor()  
        sql = "INSERT INTO Jugadores (Nombre_Jugador,id_superviviente_favorito,id_asesino_favorito) VALUES (%s, %s, %s)" 
        data = (nombre_jugador,superviviente_favorito,asesino_favorito) 
        cursor.execute(sql,data) 
        db.commit()
    return redirect(url_for('routes.formulario'))



    
    

