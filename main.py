import random

minimum = int(input("définissez les bornes, minimum: "))
maximum = int(input('maximum: '))

essai = int(input("J’ai choisi un nombre au hasard entre %d et %d."
            "\nÀ vous de le deviner..."
            "\nEntrez votre essai :" %(minimum, maximum)))

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

