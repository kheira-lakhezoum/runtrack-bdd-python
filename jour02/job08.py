import mysql.connector
import getpass

mdp = getpass.getpass("mdp :")

host = "localhost"
user = "root"
password = mdp
database = "zoo"

def connect_database():
    connexion = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    curs = connexion.cursor()
    return connexion, curs
   
def ajouter_animal(nom, race, id_cage, date_naissance, pays_origine):
    conn, cursor = connect_database()
    query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nom, race, id_cage, date_naissance, pays_origine))
    conn.commit()
    # conn.close()

def supprimer_animal(animal_id):
    conn, cursor = connect_database()
    cursor.execute('DELETE FROM animal WHERE id = %s', (animal_id,))
    conn.commit()
    # conn.close()

def modifier_animal(animal_id, nom, race, id_cage, date_naissance, pays_origine):
    conn, cursor = connect_database()
    cursor.execute('''
        UPDATE animal
        SET nom = %s, race = %s, cage_id = %s, date_naissance = %s, pays_origine = %s
        WHERE id = %s
    ''', (nom, race, id_cage, date_naissance, pays_origine, animal_id))
    conn.commit()
    # conn.close()

def afficher_animaux():
    conn, cursor = connect_database()
    cursor.execute('SELECT * FROM animal')
    animaux = cursor.fetchall()
    # conn.close()
    return animaux

def afficher_animaux_cages():
    conn, cursor = connect_database()
    cursor.execute("SELECT cage.id, cage.superficie, cage.capacite, animal.* FROM cage LEFT JOIN animal ON cage.id = animal.id_cage")
    animaux_cages = cursor.fetchall()
    for animal_cage in animaux_cages:
        print(animal_cage)

def ajouter_cage(superficie, capacite):
    conn, cursor = connect_database()
    query = "INSERT INTO cage (superficie, capacite) VALUES (%s, %s)"
    cursor.execute(query, (superficie, capacite))
    conn.commit()
    # conn.close()

def supprimer_cage(cage_id):
    conn, cursor = connect_database()
    cursor.execute('DELETE FROM cage WHERE id = %s', (cage_id,))
    conn.commit()
    # conn.close()

def modifier_cage(id_cage):
    conn, cursor = connect_database()
    cursor.execute('''
        UPDATE cage
        SET cage_id = %s
        WHERE id = %s
    ''', (id_cage))
    conn.commit()
    # conn.close()

def superficie_totale_cages():
    conn, cursor = connect_database()
    cursor.execute('SELECT SUM(superficie) FROM cage')
    superficie_totale = cursor.fetchone()[0]
    # conn.close()
    return superficie_totale

while True:
    print("\nMenu:")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    print("4. Afficher tous les animaux")
    print("5. Afficher les animaux dans les cages")
    print("6. Ajouter une cage")
    print("7. Supprimer une cage")
    print("8. Modifier une cage")
    print("9. Calculer la superficie totale des cages")
    print("0. Quitter")

    choix = input("Choisissez une option: ")

    if choix == "1":
        nom = input("Nom de l'animal: ")
        race = input("Race de l'animal: ")
        id_cage = input("ID de la cage: ")
        date_naissance = input("Date de naissance (YYYY-MM-DD): ")
        pays_origine = input("Pays d'origine: ")
        ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)

    elif choix == "2":
        animal_id = input("ID de l'animal à supprimer: ")
        supprimer_animal(animal_id)

    elif choix == "3":
        animal_id = input("ID de l'animal à modifier: ")
        nom = input("Nouveau nom de l'animal: ")
        race = input("Nouvelle race de l'animal: ")
        id_cage = input("Nouvel ID de la cage: ")
        date_naissance = input("Nouvelle date de naissance (YYYY-MM-DD): ")
        pays_origine = input("Nouveau pays d'origine: ")
        modifier_animal(animal_id, nom, race, id_cage, date_naissance, pays_origine)

    elif choix == "4":
        animaux = afficher_animaux()
        print("\nListe des animaux:")
        for animal in animaux:
            print(animal)

    elif choix == "5":
        afficher_animaux_cages()

    elif choix == "6":
        superficie = input("Superficie :")
        capacite = input("Capacite: ")
        ajouter_cage(superficie, capacite)

    elif choix == "7":
        cage_id = input("ID de la cage à supprimer: ")
        supprimer_cage(cage_id)

    elif choix == "8":
        cage_id = input("ID de la cage à modifier: ")
        modifier_cage(cage_id)

    elif choix == "9":
        superficie_totale = superficie_totale_cages()
        print("\nSuperficie totale des cages: {:.2f} m²".format(superficie_totale))

    elif choix == "0":
        print("Programme terminé.")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")

