'''
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).
'''

yritys = 0
while yritys < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus != "python" or salasana != "rules":
        yritys = yritys + 1
        print("Yritä uudelleen.")
    else:
        print("Tervetuloa.")
        break
print("Pääsy evätty.")
