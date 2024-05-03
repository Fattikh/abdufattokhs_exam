class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_title):
        self.books.append(book_title)
        self._save_to_file()

    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            self._save_to_file()
        else:
            print(f"{book_title} is not found in the library.")

    def display_books(self):
        print("Available books in the library:")
        for book in self.books:
            print(book)

    def _save_to_file(self):
        with open("books.txt", "w") as file:
            for book in self.books:
                file.write(book + "\n")

    def load_from_file(self):
        try:
            with open("books.txt", "r") as file:
                self.books = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("No library data found.")

# Example usage:
library = Library()
library.load_from_file()

library.add_book("O'tkan kunlar")
library.add_book("Dunyoning ishlari")
library.add_book("Entiklopediya")

library.display_books()

library.remove_book("Entiklopediya")

library.display_books()
