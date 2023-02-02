from app.data.modelo.jugadores import Jugador
class Jugadores_dao:



    def select_all(self,db) -> list[Jugador]:
        cursor = db.cursor()
        cursor.execute('SELECT Nombre_jugador, Nombre_Superviviente, Nombre_Asesino FROM rober.Jugadores INNER JOIN rober.Supervivientes on id_superviviente_favorito = Supervivientes.id INNER JOIN rober.Asesinos on id_asesino_favorito = Asesinos.id; ')
        jugadores_en_db = cursor.fetchall()
        jugadores_devueltos : list[Jugador] = list()
        for jugador_en_db in jugadores_en_db:
            jugadores_devueltos.append(Jugador(
            jugador_en_db[0], jugador_en_db[1], jugador_en_db[2])) 
            cursor.close()
        return jugadores_devueltos
    
    