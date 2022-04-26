class data:

    # une données est definie par un ID unique et une taille :

    def __init__(self, id, taille):
        self.id = id
        self.taille = taille
        
    def getID(self):
        return self.id
    
    def getTaille(self):
        return self.taille
