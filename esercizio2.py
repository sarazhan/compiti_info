listaA = input("Inserisci parole separate da uno spazio: ").split()
listaB =[]
for n in range (len(listaA)):
    parola = listaA[n]
    listaB.append(len(parola))
print("Ecco le loro lunghezze: ", listaB)