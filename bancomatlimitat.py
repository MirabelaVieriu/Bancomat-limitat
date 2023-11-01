from bancomatlimitat_functii import *
# Citirea sumei dorite de la utilizator
suma_dorita = int(input("Introduceți suma dorită: "))
# Citirea datelor
disponibile = citire()

#Afisare
dis=afisare(disponibile)
print(dis)

# Apelarea funcției de rezolvare și scriere în fișier
livrare, suma_livrata = rezolvare_f(disponibile, suma_dorita)

# Apelare rezolvare
rezolvare(disponibile, suma_dorita)
