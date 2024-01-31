import mysql.connector
import getpass

mdp = getpass.getpass("mdp :")

host = "localhost"  
user = "root"  
password = mdp  
database = "LaPlateforme"  

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connecté à la base de données")

        cursor = connection.cursor()
        query = "SELECT nom, capacite FROM salle"
        cursor.execute(query)

        rooms = cursor.fetchall()
        for room in rooms:
            print(f"Nom: {room[0]}, Capacité: {room[1]}")

except mysql.connector.Error as err:
    print(f"Erreur: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée")
