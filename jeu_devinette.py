import random

# Générer un nombre entre 1 et 100

nombre_secret = random.randint(1, 100)
essais = 0
trouvé = False

print("Devine le nombre mystère entre 1 et 100 !")

while not trouvé:
    try:
        proposition = int(input("Ta proposition : "))
        essais += 1

        if proposition < nombre_secret:
            print("C'est plus grand ! ")
        elif proposition > nombre_secret:
            print("C'est plus petit ! ")
        else:
            print(f" Bravo ! Tu as trouvé en {essais} essai(s).")
            trouvé = True
    except ValueError:
        print("Erreur : entre un nombre entier uniquement.")
