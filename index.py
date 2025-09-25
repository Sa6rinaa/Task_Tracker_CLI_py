import json 
from datetime import datetime

task_list = []  # liste globale pour stocker toutes les tâches
finis=[]  # liste globale pour stocker les tâches terminées



def ajouter_tache():
    try:
        # On ouvre le fichier en lecture pour récupérer les anciennes tâches
        with open("fichier.json", "r") as f:
            task_list = json.load(f)  # On charge le contenu JSON dans une liste Python
    except (FileNotFoundError, json.JSONDecodeError):
        # Si le fichier n’existe pas ou est mal formé → on repart d’une liste vide
        task_list = []

    texte = input("Saisir la tâche : ")  # Demande à l’utilisateur de saisir une nouvelle tâche

    # Générer un nouvel ID unique (si la liste n’est pas vide, on prend le dernier +1, sinon on commence à 1)
    nouvel_id = task_list[-1]["id"] + 1 if task_list else 1  

    # On crée un dictionnaire représentant une tâche
    nouvelle_tache = {
        "id": nouvel_id,  # identifiant unique
        "description": texte,  # texte saisi par l’utilisateur
        "status": "todo",  # état par défaut (à faire)
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # date de création
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")   # date de dernière modification
    }

    task_list.append(nouvelle_tache)  # On ajoute la tâche dans la liste

    # On réécrit tout le fichier JSON avec la nouvelle liste
    with open("fichier.json", "w") as f:
        json.dump(task_list, f, indent=4)

    print("Tâche ajoutée !")



def lister_tache():
    try:
        # Lire toutes les tâches depuis le fichier
        with open("fichier.json", "r") as task:
            task_list = json.load(task)
    except FileNotFoundError:
        task_list = []  # si le fichier n’existe pas
    except json.JSONDecodeError:
        print("Erreur de format JSON")
        task_list = []  # si le fichier est mal formé

    print(task_list)  # Affiche toutes les tâches brutes (non formatées)



def supprimer_tache():
    try:
        # On lit toutes les tâches
        with open("fichier.json", "r") as f:
            task_list = json.load(f)
    except FileNotFoundError:
        print("Aucune tâche à supprimer, le fichier n'existe pas.")
        return
    except json.JSONDecodeError:
        print("Erreur de format JSON dans le fichier.")
        task_list = []

    # Demande le numéro de tâche à supprimer
    task_id = int(input("Saisir l'id de la tâche à supprimer : "))

    # On filtre la liste (on garde toutes sauf celle qui correspond à l’id)
    nouvelle_liste = [t for t in task_list if t["id"] != task_id]

    # Réécriture du fichier avec la liste mise à jour
    with open("fichier.json", "w") as f:
        json.dump(nouvelle_liste, f, indent=4)

    print(f"Tâche {task_id} supprimée !")
    print("Liste actuelle des tâches :", nouvelle_liste)



def Tâche_faites():
    try:
        # Lire toutes les tâches
        with open("fichier.json", "r") as f:
            task_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        task_list = []

    # Demander quelle tâche est terminée
    task_id = int(input("Saisir l'id de la tâche terminée : "))

    trouve = False
    for tache in task_list:
        if tache["id"] == task_id:  # on cherche par id
            tache["status"] = "done"  # On met à jour le champ status
            tache["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # On met aussi la date de mise à jour
            trouve = True
            print(f"Tâche {task_id} marquée comme terminée !")
            break

    if not trouve:
        print("Tâche non trouvée.")

    # Réécrire la liste mise à jour dans le fichier
    with open("fichier.json", "w") as f:
        json.dump(task_list, f, indent=4)



# Menu principal
while True:
    choix = int(input("Lister : 1 ; Ajouter : 2 ; Supprimer : 3 ; Tâche_faites : 4 ; Quitter : 5 : "))
    if choix == 1:
        lister_tache()
    elif choix == 2:
        ajouter_tache()
    elif choix == 3:
        supprimer_tache()
    elif choix == 4:
        Tâche_faites()
    else:
        break
