from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT id, nome, indirizzo FROM biblioteca ORDER BY nome")
            biblioteche = []
            for riga in cursor:
                biblioteche.append(Biblioteca(riga["id"], riga["nome"], riga["indirizzo"]))
            cursor.close()
            return biblioteche
        except Exception as err:
            print(err)
            return None
        finally:
            cnx.close()
