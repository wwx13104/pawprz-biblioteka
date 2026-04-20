# DANE POCZĄTKOWE

books = [
    {"title": "Wiedźmin", "author": "Andrzej Sapkowski", "copies": 3},
    {"title": "Lalka", "author": "Bolesław Prus", "copies": 2},
    {"title": "Quo Vadis", "author": "Henryk Sienkiewicz", "copies": 4},
    {"title": "1984", "author": "George Orwell", "copies": 5},
    {"title": "Hobbit", "author": "J.R.R. Tolkien", "copies": 3},
]

users = {
    "ala": {"password": "1234", "role": "reader", "borrowed": []},
    "jan": {"password": "abcd", "role": "reader", "borrowed": []},
    "ola": {"password": "qwerty", "role": "reader", "borrowed": []},
}

# LOGOWANIE

def login():
    attempts = 0

    while attempts < 3:
        username = input("Login: ")
        password = input("Hasło: ")

        if username in users and users[username]["password"] == password:
            print("\nZalogowano pomyślnie!\n")
            return username

        attempts += 1
        print(f"Błędne dane ({attempts}/3)\n")

    print("Zbyt wiele prób. Koniec programu.")
    return None

# KATALOG KSIĄŻEK

def show_catalog():
    print("\n--- KATALOG KSIĄŻEK ---")
    for book in books:
        print(f"{book['title']} - {book['author']} | dostępne: {book['copies']}")
    print()

# WYPOŻYCZANIE

def borrow_book(username):
    title = input("Podaj tytuł książki: ")

    for book in books:
        if book["title"].lower() == title.lower():
            if book["copies"] > 0:
                book["copies"] -= 1
                users[username]["borrowed"].append(book["title"])
                print("Wypożyczono książkę!\n")
            else:
                print("Brak dostępnych egzemplarzy.\n")
            return

    print("Nie znaleziono książki.\n")

# MOJE WYPOŻYCZENIA

def show_my_books(username):
    print("\n--- MOJE WYPOŻYCZENIA ---")
    borrowed = users[username]["borrowed"]

    if not borrowed:
        print("Brak wypożyczonych książek.\n")
        return

    for book in borrowed:
        print(book)
    print()

# MENU

def menu(username):
    while True:
        print("1. Przeglądaj katalog")
        print("2. Wypożycz książkę")
        print("3. Moje wypożyczenia")
        print("4. Wyloguj")

        choice = input("Wybór: ")

        if choice == "1":
            show_catalog()
        elif choice == "2":
            borrow_book(username)
        elif choice == "3":
            show_my_books(username)
        elif choice == "4":
            print("Wylogowano.\n")
            break
        else:
            print("Nieprawidłowa opcja.\n")

# START PROGRAMU

def main():
    user = login()
    if user:
        menu(user)


if __name__ == "__main__":
    main()