from donnees import data
from utilisateurs import user
from noeud import node

# definition des objets :

# données :
data_1 = data(1, 200)
data_2 = data(2, 400)
data_3 = data(3, 50)
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
node_3 = node(3, 650, [], [[],[]])

node_list = [node_1, node_2, node_3]