decimale = int(input("Inserisci numero decimale: "))
resto = 0
binario = ""
binar = bin(decimale)
while decimale != 0:
    resto = str(decimale % 2)
    decimale = int(decimale / 2)
    binario = resto + binario
print ("Confronto dei risultati: ", binario,"e", binar)