pada = False
licznik_nie = 0

while not pada:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").strip().lower()

    if odpowiedz == "tak":
        print(f"Zakończono! Liczba odpowiedzi 'nie' to: {licznik_nie}")
        pada = True
    elif odpowiedz == "nie":
        licznik_nie += 1
        print("Nie pada! Yaaay!")
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Proszę podać odpowiedź: 'tak', 'nie' lub 'nie wiem'.")
