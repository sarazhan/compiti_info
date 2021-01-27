def geografia():
    diz = {}
    controllo = int(input("Quante nazioni vuoi inserire? "))
    for n in range(controllo):
        nazione = input("Inserisci la nazione: ")
        capitale = input("Inserisci la capitale della nazione: ")
        diz[nazione] = capitale

    domanda = input("Inserisci una nazione per sapere la sua capitale: ")
    if domanda not in diz:
        print("Errore: non hai inserito questa nazione nel dizionario.")
    else:
        risposta = diz[domanda]
        print(risposta)
        
geografia()

        