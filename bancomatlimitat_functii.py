def afisare(disponibile):
    for valoare, numar in disponibile:
        print(f"{numar} bancnote de {valoare} lei")
def citire():
    disponibile = []
    bancnote=[]
    with open('bancnote.txt', 'r') as input_file:
        for line in input_file:
            valoare, numar = map(int, line.strip().split())
            disponibile.append((valoare, numar))
    return disponibile

def rezolvare(disponibile, suma_dorita):
    disponibile.sort(reverse=True)
    livrare = []
    suma_livrata = 0

    for valoare, numar in disponibile:
        bancnote_livrate = min(numar, suma_dorita // valoare)
        if bancnote_livrate > 0:
            livrare.append((valoare, bancnote_livrate))
            suma_livrata += bancnote_livrate * valoare
            suma_dorita -= bancnote_livrate * valoare

    with open('rezultat.txt', 'w') as output_file:
        output_file.write("Livrare:\n")
        for valoare, numar in livrare:
            output_file.write(f"{numar} bancnote de {valoare} lei\n")
        output_file.write(f"Suma livrată: {suma_livrata} lei\n")





