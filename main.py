from tkinter import *
import mysql.connector 
from Class_stock import Stock

window = Tk() #main window
window.title("Gestion de stock") #Nom de la fenetre
window.config(bg = "#343434") #Background color



# add_button = Button(text="Ajouter un produit", font=('calibri',15),padx = 13, command=Stock.create_product, bg="#343434", fg="light grey")
# add_button.pack()

from tkinter import *
from Class_stock import Stock

window = Tk() #main window
window.title("Boutique") #Nom de la fenetre
window.config(bg = "#343434") #Background color

def create_product_window():
    # create_window = Toplevel(window)
    # create_window.title("Ajouter un produit")
    # create_window.config(bg = "#343434")

    # Création des champs de saisie
    nom_label = Label(window, text="Nom:", font=('calibri',15), bg="#343434", fg="light grey")
    nom_label.pack()

    nom_entry = Entry(window, font=('calibri',15))
    nom_entry.pack()

    description_label = Label(window, text="Description:", font=('calibri',15), bg="#343434", fg="light grey")
    description_label.pack()

    description_entry = Entry(window, font=('calibri',15))
    description_entry.pack()

    prix_label = Label(window, text="Prix:", font=('calibri',15), bg="#343434", fg="light grey")
    prix_label.pack()

    prix_entry = Entry(window, font=('calibri',15))
    prix_entry.pack()

    quantite_label = Label(window, text="Quantité:", font=('calibri',15), bg="#343434", fg="light grey")
    quantite_label.pack()

    quantite_entry = Entry(window, font=('calibri',15))
    quantite_entry.pack()

    id_cat_label = Label(window, text="Id catégorie:", font=('calibri',15), bg="#343434", fg="light grey")
    id_cat_label.pack()

    id_cat_entry = Entry(window, font=('calibri',15))
    id_cat_entry.pack()

    # Bouton Ajouter
    def add_product():
        nom = nom_entry.get()
        description = description_entry.get()
        prix = float(prix_entry.get())
        quantite = int(quantite_entry.get())
        id_cat = int(id_cat_entry.get())
        db.create_product(nom, description, prix, quantite, id_cat)
        #create_window.destroy()

    add_button = Button(window, text="Ajouter", font=('calibri',15), padx=13, command=add_product, bg="#343434", fg="light grey")
    add_button.pack()

stock = Stock() # créer une instance de la classe Stock

def add_product():
    stock.create_product() # appeler la méthode create_product() sur l'instance

add_button = Button(text="Ajouter un produit", font=('calibri',15),padx = 13, command=add_product, bg="#343434", fg="light grey")
add_button = Button(text="Ajouter un produit", font=('calibri',15), padx=13, command=create_product_window, bg="#343434", fg="light grey")
add_button.pack()

window.mainloop()


window.mainloop()