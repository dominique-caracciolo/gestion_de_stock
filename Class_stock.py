import mysql.connector 
class Stock:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin",
            database="boutique"
        )
        self.cursor = self.mydb.cursor()

    def create_product(self):
        reqsql = "INSERT INTO produit (nom, descripton, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
        values = (input("Entrez le nom du produit:"),input("Entrez la description:"),input("Entrez le prix:"),input("Entrez la quantite:"),input("Entrez l'id de categorie:"))
        self.cursor.execute(reqsql, values)
        self.mydb.commit()
        #return self.cursor.lastrowid

    def read_boutique(self):
        query = "SELECT * FROM produit"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_boutique(self, nom, descripton, prix, quantite, id_cat):
        query = "UPDATE produit SET nom=%s, description=%s, prix=%s, quantite=%s, id_categorie=%s WHERE id=%s"
        values = (nom, descripton, prix, quantite, id_cat)
        self.cursor.execute(query, values)
        self.mydb.commit()

    def delete_product(self, id):
        query = "DELETE FROM produit WHERE id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        self.mydb.commit()


db = Stock()