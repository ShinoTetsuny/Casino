import pymysql

def create_connection():
    try:
        connection = pymysql.connect(
            host="localhost",  # Remplacez par l'hôte de votre base de données
            user="root",  # Remplacez par votre nom d'utilisateur MySQL
            password="",  # Remplacez par votre mot de passe MySQL
            database="casino",  # Remplacez par le nom de votre base de données
        )
        print("Connexion réussie à la base de données")
        return connection
    except pymysql.MySQLError as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
        return None
