import noeud
import donnees

class utilisateur:
    def __init__(self, id, liste_donnees, noeud_system):
        self.id = id
        self.liste_donnees = liste_donnees
        self.noeud_system = noeud_system
        
    def getID(self):
        return self.id
    
    def getListeDonnees(self):
        return self.liste_donnees
    
    def getNoeudSystem(self):
        return self.noeud_system
    
    def afficher_utilisateur(self):
        print("Utilisateur : (" + str(self.getID()) + ", " + str(self.getListeDonnees()) + ", " + str(self.getNoeudSystem()) + ")")