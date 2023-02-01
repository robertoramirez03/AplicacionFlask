from app.data.modelo.supervivientes import Supervivientes
class Supervivientes_dao:
    def select_all(self,db) -> list[Supervivientes]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM rober.Supervivientes')
        supervivientes_en_db = cursor.fetchall()
        supervivientes : list[Supervivientes] = list()
        for supervivientes_en_db in supervivientes_en_db:
            supervivientes.append(Supervivientes(
            supervivientes_en_db[0], supervivientes_en_db[1], supervivientes_en_db[2])) 
            cursor.close()
            return supervivientes