## importation de modules
import random
#fichier à lire
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename,'r',encoding='utf-8') as f:
        l = []
        for line in f:
            lines = line.strip().split(";")
            l2 = []
            for elt in lines:
                l2.append(int(elt))
            l.append(l2)
    return l

def get_list_k(data, k):
    """retourne k-ème élément de la liste"""
    return data[k]

def get_first(l):
    """Retourne le premier élément"""
    return l[0]

def get_last(l):
    """Retourne le dernier élément"""
    return l[len(l)-1]

def get_max(l):
    """Retourne le maximum de la liste"""
    max = l[0]
    for elt in l:
        if elt>max:
            max = elt
    return max

def get_min(l):
    """Retourne le minimum de la liste"""
    min = l[0]
    for elt in l:
        if elt<min:
            min = elt
    return min

def get_sum(l):
    """Retourne la somme des éléments"""
    resultat = 0
    for elt in l :
        resultat += elt
    return resultat

#### Fonction principale

def main():
   """Fonction princpale testant les fonctions"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
        k = 37
        print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
