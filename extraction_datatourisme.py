import tkinter.filedialog as filedialog
import tkinter as tk
from tkinter import messagebox
import os
import json
import csv

#creation de fenetre
master = tk.Tk()
master.title("Extraction automatique de DataTourisme")
master.minsize(480,360)
master.iconbitmap("letter_y_icon_151235.ico")

def entree():
    """Fonction qui permet de prendre le path du dossier dans la grille"""
    entree_path = tk.filedialog.askdirectory()
    entree_entry.delete(1, tk.END)  #Efface le texte dans la grille d'input
    entree_entry.insert(0, entree_path)  # Insère le path


def sortie():
    """Fonction qui permet de choisir le dossier où on veut sauvegarder le csv"""
    sortie_path = tk.filedialog.askdirectory()
    sortie_entry.delete(1, tk.END)  #Efface le texte dans la grille d'input
    sortie_entry.insert(0, sortie_path)  # Insère le path

def extraire():
    """Fonction d'extraction"""

    pathdirectory=entree_entry.get() #Enregistre le path d'entrée dans la grille d'input dans une var
    outputdirectory=sortie_entry.get() #Enregistre le path de sauvegarde dans la grille d'input dans une var
    '''
        Met le path de chaque fichier présent dans chaque subdirectory dans une liste
    '''

    def saveFileList(pathdirectory):
        # crée une liste des dossiers et des noms des fichiers
        listOfFile = os.listdir(pathdirectory)
        allFiles = list()
        # s'applique sur chaque entrée
        for entry in listOfFile:
            # crée le path complet
            fullPath = os.path.join(pathdirectory, entry)
            # si entrée path, sauve tous les fichiers qui y sont présents dans une liste
            if os.path.isdir(fullPath):
                allFiles = allFiles + saveFileList(fullPath)
            else:
                allFiles.append(fullPath)

        return allFiles

    listefichier = saveFileList(pathdirectory)  # liste des paths pour accéder au dossier
    longueur_liste = len(listefichier)

    def listForImport(jsonfile):
        """Retourne une liste des données extraites de chaque fichier, rangés par dictionnaire pour créer le csv de template_import
        _________
        Paramètre : jsonfile :
            Le fichier où on extrait les données demandées
        Returns
        -------
        Liste rangée par dictionnaire
            Liste rangée par dictionnaire pour mettre les clés comme colonne dans le fichier csv

        Attention : nous nous référons à https://www.datatourisme.gouv.fr/ontology/core/# pour savoir à quoi correspond
        les données et où ils se trouvent
        """
        # ouverture et chargement le fichier json
        with open(jsonfile, encoding='utf-8') as f:
            data = json.load(f, encoding='utf-8')
        ##########################################

        # extraction des données avec levée des exceptions. Certaines données n'existent pas dans la base

        try:
            email = {"email": data["hasContact"][0]["schema:email"][0]}
        except KeyError:
            email = {"email": "N/A"}
        storename = {"store_name": data["rdfs:label"]["fr"][0]}
        try:
            store_phone = {"store_phone": data["hasContact"][0]["schema:telephone"][0]}
        except KeyError:
            store_phone = {"store_phone": "N/A"}
        departement = {"departement": data["isLocatedAt"][0]["schema:address"][0]
        ["hasAddressCity"]["isPartOfDepartment"]["rdfs:label"]
        ["fr"][0]}
        storecategory = {"store_category": "".join(data["@type"][0].split(":")[-1])}
        try:
            storeimage = {"store_image": data["hasRepresentation"][0]}
        except KeyError:
            storeimage = {"store_image": "N/A"}
        try:
            storeimage = {
                "store_image": data["hasRepresentation"][0]["ebucore:hasRelatedResource"][0]["ebucore:locator"][0]}
        except KeyError:
            storeimage = {"store_image": "N/A"}
        try:
            geoadress = {"geo_adress": "".join(data["isLocatedAt"][0]["schema:address"][0]
                                               ["schema:streetAddress"][0]) + " " + "".join(data["isLocatedAt"][0]
                                                                                            ["schema:address"][0][
                                                                                                "schema:addressLocality"])}
        except KeyError:
            geoadress = {"geo_adress": "Voie N/A" + " " + "".join(data["isLocatedAt"][0]
                                                                  ["schema:address"][0]["schema:addressLocality"])}
        try:
            department = {
                "department": data["isLocatedAt"][0]["schema:address"][0]["hasAddressCity"]["isPartOfDepartment"]
                ["rdfs:label"]["fr"][0]}
        except KeyError:
            department = {"department": "N/A"}
        try:
            description = {"description": data["hasDescription"][0]["dc:description"]
            ["fr"][0]}
        except KeyError:
            description = {"description": "N/A"}
        try:
            email = {"email": data["hasContact"][0]["schema:email"][0]}
        except KeyError:
            email = {"email": "N/A"}
        try:
            store_website = {"store_website": data["hasContact"][0]["foaf:homepage"][0]}
        except KeyError:
            store_website = {"store_website": "N/A"}
        try:
            numdep = {"numdep": data["isLocatedAt"][0]["schema:address"][0]["hasAddressCity"]["insee"]}
        except KeyError:
            numdep = {"numdep": "N/A"}

        ###############################################

        # sauvegarde clés et valeurs dans un dictionnaire
        dict1 = {**storename, **email, **store_phone, **storecategory, **geoadress, **department, **storeimage,
                 **description, **store_website,
                 **numdep}
        ###############################################

        # ajout dictionnaire dans la liste
        data_list.append(dict1)
        return (data_list)

    data_list = []
    """Itération de la fonction sur chaque fichier présent dans liste listefichier"""
    # variable à incrémenter
    i = -1
    # tant que i est inférieur à la longueur de la liste, on va appliquer la fonction sur chaque élément de la liste
    while i < longueur_liste-1:
        i += 1
        listForImport(listefichier[i])
    toCSV = data_list  # variable toCSV pour facilité de lecture
    """"création d'un fichier CSV à partir de la liste où se trouvent les données extraites
    en prenant en colonne les clés de dictionnaire"""
    # permet d'avoir les clés de dictionnaire
    keys = toCSV[0].keys()
    #########################################

    # crée le fichier csv
    with open(outputdirectory, 'w', newline='', encoding='utf-8')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)
    tk.messagebox.showinfo('Extraction DataTourisme', 'Extraction terminée')

#Création des cadres où seront mis les différents éléments
top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

#Création des boutons et éléments visuels

entree_path = tk.Label(top_frame, text="Chemin des fichiers:\n exemple : C:/Users/moi/OneDrive/Bureau/flux-9185-202101190156/objects")
entree_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Parcourir", command=entree)

sortie_path = tk.Label(bottom_frame, text="Chemin de sauvegarde du fichier csv:\n exemple : C:/Users/moi/OndeDrive/Bureau/extraction.csv")
sortie_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Parcourir", command=sortie)

extract_button = tk.Button(bottom_frame, text='Extraire', command=extraire)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

entree_path.pack(pady=5)
entree_entry.pack(pady=5)
browse1.pack(pady=5)

sortie_path.pack(pady=5)
sortie_entry.pack(pady=5)
browse2.pack(pady=5)

extract_button.pack(pady=20, fill=tk.X)


master.mainloop()