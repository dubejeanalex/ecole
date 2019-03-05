#Créer un programme PYTHON pour insérer un employé
#Créer un script PYTHON qui demande à l'utilisateur un numéro d'employé,
# un nom et un prénom et qui l'insère dans la table employé.
#Le script s'exécute jusqu'à ce que l'utilisateur entre le numéro d'employé 0.

import sqlite3

connexion = sqlite3.connect('C:/DB/specialiste.db')
curseur = connexion.cursor()
requete = "INSERT INTO employe( nom, prenom,noEmploye)VALUES ( 'peltier', 'sebastien', 120022);"
curseur.execute(requete)
#requete = "SELECT * FROM employe"

#curseur.execute(requete)

#liste =curseur.fetchall()
#print (liste)

estFini=False

while estFini==False:

    nom = input("Quelle est votre nom")

    prenom = input("Quelle est votre prénom ?")

    numeroEmploye=input("Quel est votre numéro employé ?")
    data=(nom,prenom,numeroEmploye)

    for tuple in data:
        curseur.execute("INSERT INTO employe( nom,prenom,noEmploye)VALUES  (?,?,?);")


    connexion.commit()

    choix=input("Veuillez entrer 0 si vous avez terminé.")
    if choix=="0":
        estFini=True
        print(nom, prenom,numeroEmploye, "  a bien été ajouté.")
    else:
        estFini=False
        print (nom,prenom,numeroEmploye, "  false dans mon else.")

requete="SELECT * FROM employe"
curseur.execute(requete)
liste=curseur.fetchall()
print (liste)



