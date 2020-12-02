lunghezza = int(input("Quanto è lungo il tuo numero binario? "))
binario = ""
decimale = 0
for n in range(lunghezza):
    print ("La", n+1, "° partendo da destra ")
    cifra = input()
    binario = cifra + binario
    cifra = int(cifra)
    decimale = decimale + (cifra*(2**n))
binario = int(binario, 2)
print ("Confronto dei risultati:", binario,"e", decimale)