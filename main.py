#Ulysse Doyon
import random

#définir les bornes (fonction)
def bornes():
    minimum = int(input("définissez les bornes, minimum: "))
    maximum = int(input("définissez les bornes, maximum: "))
    aleatoire = random.randint(minimum, maximum)
    print("J’ai choisi un nombre au hasard entre %d et %d."
        "\nÀ vous de le deviner..."% (minimum, maximum))
    return aleatoire
#premier essai
chiffre_aleatoire = bornes()
essai = int(input("Entrez votre essai :"))

#boucle d'essai (while)
nb_essais = 0
boucle = True
while boucle:
    if essai == chiffre_aleatoire:
        print("bravo! Vous avez terminé avec %d essais" %(nb_essais))
        boucle = False
#fin

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
