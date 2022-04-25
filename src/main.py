from donnees import data
from utilisateurs import user
from noeud import node

#__________________________________________________________________________
# definition des objets :
#__________________________________________________________________________

# données :
data_1 = data(1, 50)
data_2 = data(2, 250)
data_3 = data(3, 150)
data_4 = data(4, 100)

data_list = [data_1, data_2, data_3, data_4]

# utilisateurs :
user_1 = user(1, [1, 3])
user_2 = user(2, [2])
user_3 = user(3, [])

user_list = [user_1, user_2, user_3]

# noeuds :
node_1 = node(1, 300, [], [[],[]])
node_2 = node(2, 50, [], [[],[]])
node_3 = node(3, 100, [], [[],[]])
node_4 = node(4, 500, [], [[],[]])

node_list = [node_1, node_2, node_3, node_4]

# ajout complémentaires :
node_list[0].addUser(user_list[0])
node_list[2].addUser(user_list[1])

node_list[0].addNodeVoisin(node_list[1])
node_list[0].addNodeVoisin(node_list[2])
node_list[1].addNodeVoisin(node_list[0])
node_list[1].addNodeVoisin(node_list[2])
node_list[2].addNodeVoisin(node_list[0])
node_list[2].addNodeVoisin(node_list[1])
node_list[2].addNodeVoisin(node_list[3])
node_list[3].addNodeVoisin(node_list[2])

user_list[0].addNode(node_list[0])
user_list[1].addNode(node_list[2])


#__________________________________________________________________________
# fonctions
#__________________________________________________________________________

# fonction qui donne à tous les utilisateurs, un systeme de noeud qui contient toutes les données dont ils ont besoins :
def needData():
    for user in user_list:
        if user.getNoeudSystem() != None :
            node_sys = user.getNoeudSystem()

            if user.getNotStockedData() != [] :
                node_sys.getListeDonneesLocals.append(user.getNotStockedData()[0])
                user.addData(user.getListeDonnees()[0])