import random

poprawna_odpowiedz = False
while not poprawna_odpowiedz:
    pogoda = random.choice(["Pada", "Nie pada"])
    print("Czy pada? (tak/nie)")
    odpowiedz = input().strip().lower()
    
    if (pogoda == "Pada" and odpowiedz == "tak") or (pogoda == "Nie pada" and odpowiedz == "nie"):
        print("Brawo użytkowniku, zgadłes, dobra robota :)")
        poprawna_odpowiedz = True
        break
    else:
        print("Niestety użytkowniku nie odblokowałeś osiągniecia zgadniecia pogody, nie przejmuj sie możesz spróbować ponownie. Powodzenia!")
