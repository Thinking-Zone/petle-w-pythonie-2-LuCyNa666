while True:
    odpowiedz = input("Czy wypiłeś już dzisiaj wodę? (tak/nie/nie wiem): ").strip().lower()

    if odpowiedz == "tak":
        print("Masz super poziom nawodnienia, brawo użytkowniku!")
        break
    elif odpowiedz == "nie":
        print("It's time to drink water użytkowniku")
    elif odpowiedz == "nie wiem":
        print("To napij się wody bo pomaga na pamięć użytkowniku")
    else:
        print("Chyba wypiłeś za mało wody jeżeli nie umiesz po prostu odpowiedzieć: 'tak', 'nie' lub 'nie wiem'.")
