from flask import Blueprint, render_template, request

from app import db
#from app.data.equipo_dao import EquipoDao
rutas_usuarios = Blueprint("routes", __name__)

@rutas_usuarios.route("/")
def index():
    return render_template("index.html")

@rutas_usuarios.route("/formulario")
def formulario():
    return render_template("formulario.html")


@rutas_usuarios.route('/formulario_supervivientes', methods=['POST'])
def formulario_supervivientes():
    nombre_jugador = request.form['nombre_jugador'] 
    superviviente_favorito = request.form['superviviente_favorito'] 
    color_de_pelo = request.form['color_de_pelo']
    asesino_favorito = request.form['asesino_favorito']
    metros_por_segundo = request.form['metros_por_segundo']

    if (nombre_jugador and superviviente_favorito and color_de_pelo and asesino_favorito and metros_por_segundo):
        cursor = db.database.cursor()  
        sql = "INSERT INTO Jugadores (Nombre_Jugador,Superviviente_Favorito,Color_Pelo,Asesino_Favorito,Metros_Por_Segundo) VALUES (%s, %s, %s, %s, %s)" 
        data = (nombre_jugador,superviviente_favorito,color_de_pelo,asesino_favorito,metros_por_segundo) 
        cursor.execute(sql,data) 
        db.database.commit() 
    
    

