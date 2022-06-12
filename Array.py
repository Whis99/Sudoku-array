
class Tableau:
    """simple classe de tableau personalisé."""

    types = {"i": int, "b": bool, "s": str, "f": float}

    def __init__(self, datatype,  largeur=10):
        self.largeur = largeur
        self.datatype = datatype
        self.tableau = [0 for _ in range(largeur)]
        self.prochainIndex = 0

    def __repr__(self):
        rep = f'(Tableau({self.datatype}, {self.largeur})'
        return rep

    def append(self, valeur):
        """
         Cette fonction ajoute une valeur dans un tableau. 
         S'il n'a pas assez de place dans le tableau, 
         un nouveau tableau de largeur double est créé. 
        """
        if self.prochainIndex == self.largeur:
            tempArr = [0 for _ in range(self.largeur * 2)]

            for index, val in enumerate(self.tableau):
                tempArr[index] = val
            self.nextIndex = index + 1
            self.tableau = tempArr
            self.largeur *= 2
        # Todo: vérifier si le typage de la valeur au datatype de l'object.
        # Par exemple si le "datatype est "s" tous les éléments dans le tableau seront du type str.
        # Sinon on retourne un message "Erreur de typage: les éléments doivent être du type str".
        if type(valeur) != Tableau.types[self.datatype]:
            return f'Type Error! Array type is {Tableau.types[self.datatype]} not {type(valeur)}'
        self.tableau[self.prochainIndex] = valeur
        self.prochainIndex += 1
        return self.tableau

    def length(self):
        """ retourne la quantité d'éléments présent dans le tableau """
        # TODO
        return (self.prochainIndex )

    def remove(self):
        """ élimine le dernier élément du tableau et retourne le tableau"""
        # TODO
        tab_ind = self.prochainIndex - 1
        self.tableau[tab_ind] = 0
        self.prochainIndex -= 1
        return self.tableau

    def removeAt(self, position):
        """
        élimine l'élimine l'élément qui se trouve a la position (index) donnée et retourne le tableau.
        """
        # TODO
        if self.tableau[position + 1] == 0:
            self.tableau[position] = 0
            self.prochainIndex -= 1
        else:
            for i in range(position, self.prochainIndex + 1):
                self.tableau[i] = self.tableau[i + 1]
                self.prochainIndex -= 1
        return self.tableau

    def retrieve(self, position):
        """
        retourne l'élément qui se trouve à la position donnée.
        """
        # TODO
        element = self.tableau[position]
        return element

    def sort(self):
        """ trie le tableau en place (O(1) d'espace) et retourne le tableau.
        """
        # TODO
        for i in range(1, self.prochainIndex + 1):
            key = self.tableau[i]  # Put the first element of the array as a key
            j = i - 1  # j got index of 0 to start
            while j >= 0 and key < self.tableau[j]:
                self.tableau[j + 1] = self.tableau[j]
                j -= 1
            self.tableau[j + 1] = key
        return self.tableau

