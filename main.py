import random

chiffre_aleatoire = random.randint(1, 100)
essai = int(input("J’ai choisi un nombre au hasard entre 1 et 100."
            "\nÀ vous de le deviner..."
            "\nEntrez votre essai :"))

boucle = True
while boucle:
    if essai == chiffre_aleatoire:
        print("bravo!")
        boucle = False

    elif essai < chiffre_aleatoire:
        print("chiffre plus petit")
        essai = int(input("nouveau essai:"))

    elif essai > chiffre_aleatoire:
        print("chiffre plus grand")
        essai = int(input("nouveau essai:"))

    else:
        pass