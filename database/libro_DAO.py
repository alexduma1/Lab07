from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        try:
            cursor = cnx.cursor()
            cursor.execute(
                "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere"
            )
            generi = []
            for riga in cursor:
                generi.append(riga[0])
            cursor.close()
            return generi
        except Exception as err:
            print(err)
            return None
        finally:
            cnx.close()

    def get_libri_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(
                "SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca "
                "FROM libro l JOIN biblioteca b ON l.id_biblioteca = b.id "
                "WHERE b.nome = COALESCE(%s, b.nome) AND l.genere = COALESCE(%s, l.genere) "
                "ORDER BY l.titolo",
                (biblioteca, genere)
            )
            libri = []
            for riga in cursor:
                libri.append(Libro(
                    riga["id"],
                    riga["titolo"],
                    riga["autore"],
                    riga["genere"],
                    riga["anno_pubblicazione"],
                    riga["id_biblioteca"]
                ))
            cursor.close()
            return libri
        except Exception as err:
            print(err)
            return None
        finally:
            cnx.close()
