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
        query = "SELECT SUM(capacite) AS capacite_totale FROM salle"
        cursor.execute(query)

        total_capacite = cursor.fetchone()[0]
        print(f"La capacité totale des salles est de {total_capacite}")

except mysql.connector.Error as err:
    print(f"Erreur: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée")




    
