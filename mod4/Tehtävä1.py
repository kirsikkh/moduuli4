#Kirjoita while-toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.


luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(f"{luku} on jaollinen kolmella.")
    luku = luku + 1

    #else:
       # print(f"{luku} ei ole jaollinen kolmella.")
'''
Tulostetaan kertotaulu yhdestä viiteen.
Mukaan otetaan siis kaikki 25 erilaista tuloa, joissa tulon tekijät ovat 1, 2, 3, 4 tai 5:

eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1
'''
