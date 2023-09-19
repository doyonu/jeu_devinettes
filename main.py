import random

a = int(input("définissez les bornes, minimum: "))
b = int(input('maximum: '))

chiffre_aleatoire = random.randint(a, b)
essai = int(input("J’ai choisi un nombre au hasard entre 1 et 100."
            "\nÀ vous de le deviner..."
            "\nEntrez votre essai :"))

nb_essais = 0
boucle = True
while boucle:
    if essai == chiffre_aleatoire:
        print("bravo! Vous avez terminé avec %d essais" %(nb_essais))
        boucle = False

    elif essai > chiffre_aleatoire:
        print("chiffre plus petit")
        essai = int(input("nouveau essai:"))
        nb_essais += 1

    elif essai < chiffre_aleatoire:
        print("chiffre plus grand")
        essai = int(input("nouveau essai:"))
        nb_essais += 1

    else:
        pass
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