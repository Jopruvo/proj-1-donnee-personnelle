import donnees

class noeud:
    def __init__(self, id, capacite_memoire, liste_donnees_locals, liste_access):
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

    def afficher_noeud(self):
        print("Noeud sytème : (" + str(self.getID()) + ", " + str(self.getCpMem()) + ", " + str(self.getListeDonneesLocals()) + ", " + str(self.getListeAccess()) + ")")   
