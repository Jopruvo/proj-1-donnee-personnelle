class donnees:
    def __init__(self, id, taille):
        self.id = id
        self.taille = taille
        
    def getID(self):
        return self.id
    
    def getTaille(self):
        return self.taille
    
    def afficher_donnees(self):
        print("Données : (" + str(self.getID()) + ", " + str(self.getTaille()) + ")")