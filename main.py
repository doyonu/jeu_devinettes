#Ulysse Doyon
import random
choix = "oui"
nb_essais = 1

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
while choix == "oui":

#chiffre trop grand
    if essai > chiffre_aleatoire:
        print("chiffre plus petit")
        essai = int(input("nouveau essai:"))
        nb_essais += 1

#chiffre trop petit
    elif essai < chiffre_aleatoire:
        print("chiffre plus grand")
        essai = int(input("nouveau essai:"))
        nb_essais += 1

    else:
        print("bravo! Vous avez terminé avec %d essais" % (nb_essais))
#choix recommencer
        choix = input("voulez-vous recommencer?")
        if choix == "oui":
            chiffre_aleatoire = bornes()
            essai = 0
        else:
            pass
print("au revoir")