Lista_numeri = []
nonmulti3 = []
ripetizione = int(input("Quanti numeri vuoi inserire? "))
for n in range(ripetizione):
    numero = int(input("Inseisci un numero casuale tra 1 e 30: "))
    Lista_numeri.append(numero)
for n, i in enumerate(Lista_numeri):
        print(n, i )
multipli3 = [n for n in Lista_numeri if n%3 == 0]
for n in Lista_numeri:
    if n not in multipli3:
        nonmulti3.append(n)
print(nonmulti3)