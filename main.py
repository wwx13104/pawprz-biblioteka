class Book:
    def __init__(self, title, author, total_copies):
        self._title = title
        self._author = author
        self._total_copies = total_copies
        self._available_copies = total_copies

    def borrow(self):
        if self._available_copies > 0:
            self._available_copies -= 1
            return True
        return False

    def return_book(self):
        if self._available_copies < self._total_copies:
            self._available_copies += 1

    def __str__(self):
        return f"{self._title} - {self._author} | dostępne: {self._available_copies}"

    @property
    def title(self):
        return self._title


class User:
    def __init__(self, login, password, role):
        self._login = login
        self._password = password
        self._role = role

    def check_password(self, password):
        return self._password == password

    @property
    def login(self):
        return self._login

    @property
    def role(self):
        return self._role


class Reader(User):
    def __init__(self, login, password):
        super().__init__(login, password, "reader")
        self._borrowed = []
        self._requests = []

    def borrow_book(self, book):
        if book.borrow():
            self._borrowed.append(book)
            return True
        return False

    def get_borrowed(self):
        return self._borrowed

    def request_extension(self, book):
        if book in self._borrowed:
            self._requests.append(book)
            return True
        return False

    def get_requests(self):
        return self._requests


class Librarian(User):
    def __init__(self, login, password):
        super().__init__(login, password, "librarian")


class Library:
    def __init__(self):
        self._books = []
        self._users = []
        self._extension_requests = []

    def add_book(self, book):
        self._books.append(book)

    def add_user(self, user):
        self._users.append(user)

    def find_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_user(self, login):
        for user in self._users:
            if user.login == login:
                return user
        return None

    def borrow_book(self, reader, title):
        book = self.find_book(title)
        if not book:
            return "Nie znaleziono książki"
        if reader.borrow_book(book):
            return "Wypożyczono"
        return "Brak dostępnych egzemplarzy"

    def list_books(self):
        for book in self._books:
            print(book)

    def list_all_borrowings(self):
        for user in self._users:
            if isinstance(user, Reader):
                for book in user.get_borrowed():
                    print(f"{book.title} - wypożyczone przez {user.login}")

    def add_extension_request(self, reader, title):
        book = self.find_book(title)
        if book and reader.request_extension(book):
            self._extension_requests.append((reader, book))
            return "Prośba wysłana"
        return "Nie można wysłać prośby"

    def handle_requests(self):
        for i, (reader, book) in enumerate(self._extension_requests):
            print(f"{i}. {book.title} - {reader.login}")

        choice = int(input("Wybierz numer (-1 aby wyjść): "))
        if choice == -1:
            return

        decision = input("Akceptować (t/n): ")

        if decision == "t":
            print("Zaakceptowano")
        else:
            print("Odrzucono")

        self._extension_requests.pop(choice)


library = Library()

library.add_book(Book("Wiedźmin", "Sapkowski", 3))
library.add_book(Book("Lalka", "Prus", 2))
library.add_book(Book("1984", "Orwell", 4))
library.add_book(Book("Hobbit", "Tolkien", 5))
library.add_book(Book("Quo Vadis", "Sienkiewicz", 3))

library.add_user(Reader("ala", "1234"))
library.add_user(Reader("jan", "abcd"))
library.add_user(Librarian("admin", "admin"))


def login():
    for _ in range(3):
        login = input("Login: ")
        password = input("Hasło: ")

        user = library.find_user(login)
        if user and user.check_password(password):
            return user

        print("Błędne dane")

    return None


def reader_menu(user):
    while True:
        print("1. Katalog")
        print("2. Wypożycz")
        print("3. Moje książki")
        print("4. Prośba o przedłużenie")
        print("5. Wyloguj")

        c = input("Wybór: ")

        if c == "1":
            library.list_books()
        elif c == "2":
            t = input("Tytuł: ")
            print(library.borrow_book(user, t))
        elif c == "3":
            for b in user.get_borrowed():
                print(b)
        elif c == "4":
            t = input("Tytuł: ")
            print(library.add_extension_request(user, t))
        elif c == "5":
            break


def librarian_menu(user):
    while True:
        print("1. Lista wypożyczeń")
        print("2. Obsługa próśb")
        print("3. Wyloguj")

        c = input("Wybór: ")

        if c == "1":
            library.list_all_borrowings()
        elif c == "2":
            library.handle_requests()
        elif c == "3":
            break


def main():
    while True:
        user = login()
        if not user:
            break

        if user.role == "reader":
            reader_menu(user)
        else:
            librarian_menu(user)


if __name__ == "__main__":
    main()