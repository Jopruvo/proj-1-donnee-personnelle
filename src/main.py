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
        if user.getNoeudSystem() != None:
            node_sys = user.getNoeudSystem()
            if user.getNotStockedData() != []:
                node_sys.setListeDonneesLocals(user.getNotStockedData()[0])
                user.addData(user.getListeDonnees()[0])

needData()


# fonction qui prend les noeuds vides et les ajoutes à une liste :
def getEmptyNode(nodeList):
    empty_node = []
    for node in nodeList:
        if node.getListeDonneesLocals() == None:
            empty_node.append(node)
    return empty_node


# fonction qui donne à tous les noeuds les data et les place en fonction de l'interet des utilisateurs :
def getData():
    for user in user_list:
        node_sys = user.getNoeudSystem()
        if user.getNotStockedData() != []:
            empty_node_voisin = getEmptyNode(node_sys.getListeAccessVoisin())
            if empty_node_voisin != []:
                empty_node_voisin[0].setListeDonneesLocals(user.getNotStockedData()[0])
                user.addData(user.getNotStockedData()[0])
                print('Le noeud voisin vide de ' + str(node_sys.getID()) + ' est ' + str(empty_node_voisin[0].getID()))
                print(empty_node_voisin[0].getListeDonneesLocals())


# fonction de distribution du reste des données :
def distrib():
    empty_nodes = getEmptyNode(node_list)
    for user in user_list:
        if user.getNotStockedData() != []:
            for d in user.getNotStockedData():
                empty_nodes[0].setListeDonneesLocals(d)
                empty_nodes.remove(empty_nodes[0])
                user.addData(user.getListeDonnees()[0])
    for i in node_list:
        print('Node : ' + str(i.getID()) + ' contient les data : ' + str(i.getListeDonneesLocals()))
