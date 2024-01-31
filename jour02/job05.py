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
        query = "SELECT SUM(superficie) AS superficie_totale FROM etage"
        cursor.execute(query)

        total_superficie = cursor.fetchone()[0]
        print(f"La superficie de La Plateforme est de {total_superficie} m2")

except mysql.connector.Error as err:
    print(f"Erreur: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée")
