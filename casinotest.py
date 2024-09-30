import pymysql
from db_connection import create_connection

# Établir une connexion à la base de données
db = create_connection()
def createUser():
    if db:
        # Créer un objet curseur pour interagir avec la base de données
        cursor = db.cursor()

        # Définir la requête SQL pour insérer un nouvel utilisateur
        query = "INSERT INTO user (name_user, date, average_try, average_putting, last_level) VALUES (%s, %s, %s, %s, %s)"

        # Demander à l'utilisateur de saisir les données
        name_user = input("Entrez le nom d'utilisateur: ")
        date = input("Entrez la date (AAAA-MM-JJ): ")
        average_try = float(input("Entrez le nombre d'essais moyen: "))
        average_putting = float(input("Entrez la mise moyenne: "))
        last_level = int(input("Entrez le dernier niveau: "))

        try:
            # Exécuter la requête avec les données de l'utilisateur
            cursor.execute(query, (name_user, date, average_try, average_putting, last_level))

            # Valider les modifications dans la base de données
            db.commit()
            print("Les données ont été insérées avec succès.")
        except pymysql.MySQLError as e:
            print(f"Erreur lors de l'insertion des données : {e}")
            db.rollback()  # Si une erreur survient, annuler la transaction

        # Fermer le curseur et la connexion à la base de données
        cursor.close()
        db.close()
    else:
        print("Impossible d'établir la connexion à la base de données.")
