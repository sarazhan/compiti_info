Lista_parola = input("Scrivi una parola separata dagli spazi es. c i a o : ").split()
if Lista_parola == Lista_parola.reverse():
    print("La parola inserita è pandroma")
else:
    print("La parola inserita è palindroma")