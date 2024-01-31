import mysql.connector
import getpass

mdp = getpass.getpass("mdp :")

class Employe:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.connection.commit()

    def read_employe(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:
            print(i)
            
    def update_employe_salary(self, employe_id, new_salary):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salary, employe_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_employe(self,id):
        query = "DELETE FROM employe WHERE id=%s"
        values=(id,)
        self.cursor.execute(query, values)
        self.connection.commit()

employe = Employe("localhost", "root", mdp, "employe")

# employe.create_employe()

# employe.update_employe_salary()

# employe.delete_employe()

employe.read_employe()


