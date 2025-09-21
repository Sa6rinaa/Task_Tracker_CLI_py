import json 

task_list = []  # liste globale pour stocker toutes les tâches
finis=[]  # liste globale pour stocker les tâches terminées





def ajouter_tache():
    try:
        with open("fichier.json", "r") as f:
            task_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        task_list = []

    texte = input("Saisir la tâche : ")
    nouvelle_tache = {"nom": texte, "terminee": False}  # ✅ dictionnaire
    task_list.append(nouvelle_tache)

    with open("fichier.json", "w") as f:
        json.dump(task_list, f, indent=4)

    print("Tâche ajoutée !")


def lister_tache():
    try :
        with open("fichier.json", "r") as task :
            task_list = json.load(task)   
    except FileNotFoundError:
        task_list = []                      # si le fichier n'existe pas, on crée une liste vide
    except json.JSONDecodeError:
        print("Erreur de format JSON")
        task_list = []                      # liste vide si le JSON est mal formé
    print(task_list)          # on affiche la liste actuelle   




def supprimer_tache():
    # 1️⃣ Lire le fichier JSON
    try:
        with open("fichier.json", "r") as f:
            task_list = json.load(f)
    except FileNotFoundError:
        print("Aucune tâche à supprimer, le fichier n'existe pas.")
        return
    except json.JSONDecodeError:
        print("Erreur de format JSON dans le fichier.")
        task_list = []

    # 2️⃣ Demander à l'utilisateur quelle tâche supprimer
    task = input("Saisir la tâche à supprimer : ")

    # 3️⃣ Vérifier si la tâche existe
    if task in task_list:
        task_list.remove(task)
        # 4️⃣ Réécrire la liste mise à jour dans le JSON
        with open("fichier.json", "w") as f:
            json.dump(task_list, f)
        print(f"Tâche '{task}' supprimée !")
    else:
        print(f"Tâche '{task}' non trouvée.")

    # 5️⃣ Afficher la liste actuelle
    print("Liste actuelle des tâches :", task_list)

    

def Tâche_faites():
    try:
        with open("fichier.json", "r") as f:
            task_list = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        task_list = []

    # Demander quelle tâche est terminée
    nom_tache = input("Saisir la tâche terminée : ")

    # Chercher dans la liste
    trouve = False
    for tache in task_list:
        if tache["nom"] == nom_tache:
            tache["terminee"] = True   # ✅ on met à jour le champ
            trouve = True
            print(f"Tâche '{nom_tache}' marquée comme terminée !")
            break

    if not trouve:
        print("Tâche non trouvée.")

    # Réécrire la liste dans le fichier
    with open("fichier.json", "w") as f:
        json.dump(task_list, f, indent=4)





while True:
    choix=int(input("Lister : 1 ; Ajouter : 2 ; Supprimer : 3 ; Tâche_faites : 4 ; ; Quitter : 5:"))
    if choix==1:
      lister_tache()
    elif choix==2 :
        ajouter_tache()    
    elif choix==3 :
        supprimer_tache() 
    elif choix==4 :
        Tâche_faites() 
    else :
        break