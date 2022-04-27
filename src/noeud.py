class node:

    # un noeud est défini par un ID unique, la capacité mémoire d'un noeud (dans lequel il a la capacité d'acceuillir un ou plusieurs
    # objets de type 'donnees'), une liste de données stockées, et une liste de liste (ou tableau) dans lequel la première est une liste
    # d'ID 'utilisateurs qui y ont accés et la seconde une liste de noeud voisins :

    def __init__(self, id, capacite_memoire, liste_donnees_locals = [], liste_access = [[],[]]):
        self.id = id
        self.capacite_memoire = capacite_memoire
        self.liste_donnees_locals = liste_donnees_locals
        self.liste_access = liste_access
        
    def getID(self):
        return self.id
    
    def getCpMem(self):
        return self.capacite_memoire
    
    def getListeDonneesLocals(self):
        return self.liste_donnees_locals
    
    def getListeAccess(self):
        return self.liste_access

    def getListeAccessUsers(self):
        return self.liste_access[0]

    def getListeAccessVoisin(self):
        return self.liste_access[1]

    def addUser(self, user):
        self.liste_access[0].append(user)

    def addNodeVoisin(self, node):
        self.liste_access[1].append(node)

    def setListeDonneesLocals(self, liste_donnees_locals):
        self.liste_donnees_locals = liste_donnees_locals

    def setListeAccessible(self, liste_access):
        self.liste_access = liste_access
