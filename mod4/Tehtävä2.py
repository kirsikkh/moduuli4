'''
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
'''

tuuma = 0
while tuuma >= 0:
    tuuma = int(input("Anna tuumamäärä: "))
    print(f"{tuuma} tuumaa on {tuuma*2.54} centtimetriä.")

