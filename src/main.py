import donnees
import utilisateurs
import noeud

class Tree:
    def __init__(self, node):
        self.node = node
    
    def getNode(self):
        return self.node
    
    def afficherTree(self):
        print('Tree : (' + str(self.getNode()) + ')')

data_1 = donnees.donnees(1, 200)
data_2 = donnees.donnees(2, 400)
data_3 = donnees.donnees(3, 50)
data_4 = donnees.donnees(4, 100)

noeud_1 = noeud.noeud(1, 250, [], [[1],[]])
noeud_2 = noeud.noeud(2, 402, [], [[2],[]])
noeud_3 = noeud.noeud(3, 150, [], [[3],[]])

nodeTree = Tree([noeud_1, noeud_2, noeud_3])

user_1 = utilisateurs.utilisateur(1, [data_1, data_2, data_3, data_4], noeud_1.getID())
user_2 = utilisateurs.utilisateur(2, [data_2, data_4], noeud_2.getID())