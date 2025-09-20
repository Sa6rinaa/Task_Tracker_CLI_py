import json 

task_list = []  # liste globale pour stocker toutes les tâches
finis=[]  # liste globale pour stocker les tâches terminées




def ajouter_tache():
    try :
        with open("fichier.json", "r") as task :
            task_list = json.load(task)   
    except FileNotFoundError:
        task_list = []                      # si le fichier n'existe pas, on crée une liste vide
    except json.JSONDecodeError:
        print("Erreur de format JSON")
        task_list = []                      # liste vide si le JSON est mal formé


    task = input("Saisir la tâche : ")
    task_list.append(task)   # on ajoute la tâche à la liste globale
    print(task_list)          # on affiche la liste actuelle
    
    with open("fichier.json", "w") as f:
        json.dump(task_list, f)
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
        with open("fichier.json", "r") as terminer :
            finis = json.load(terminer)   
    except FileNotFoundError:
        finis = []                      # si le fichier n'existe pas, on crée une liste vide
    except json.JSONDecodeError:
        print("Erreur de format JSON")
        finis = []                      # liste vide si le JSON est mal formé
    print(terminer)          # on affiche la liste actuelle



    terminer=input("Saisir la tâche terminée : ")
    finis.append(terminer)
    print(finis)

with open("fichier.json", "w") as f:
        json.dump(finis, f)
        print("Tâche TERMINER !")





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