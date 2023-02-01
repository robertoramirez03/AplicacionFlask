from flask import Blueprint, render_template, request,  redirect, url_for

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
    datos_services = supervivientes_dao(db.session)
    return render_template("datos.html,")





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


@rutas_usuarios.route('/datos') 
def notas():
    cursor = db.cursor()
    cursor.execute("SELECT i.Nombre,n.CodigoAlumno,n.Seguridad,n.Implantacion,n.Redes FROM Notas n INNER JOIN InformacionAlumno i on n.CodigoAlumno = i.CodigoAlumno")
    myresult = cursor.fetchall() 
    insertObject = [] 
    columnNames = [column[0] for column in cursor.description] 
    for record in myresult:  
        insertObject.append(dict(zip(columnNames,record))) 
    cursor.close() 
    
    

