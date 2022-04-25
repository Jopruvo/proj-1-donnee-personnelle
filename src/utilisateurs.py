class utilisateur:

    # un utilisateur est défini à l'aide d'un ID unique, par une liste de données auxquelles il peut accéder
    # et un noeud qui lui est accessible :

    def __init__(self, id, liste_donnees, noeud_system = None):
        self.id = id
        self.liste_donnees = liste_donnees
        self.noeud_system = noeud_system
        self.notStockedData = liste_donnees    # permet plus facilement de traiter les données interressé par un utilisateur plutot que de manipuler liste_donnees
        
    def getID(self):
        return self.id
    
    def getListeDonnees(self):
        return self.liste_donnees
    
    def getNoeudSystem(self):
        return self.noeud_system

    def addNode(self, node):
        self.noeud_system = node

    def getNotStockedData(self):
        return self.notStockedData

    def addData(self, data):
        if data in self.notStockedData:
            self.notStockedData.remove(data)