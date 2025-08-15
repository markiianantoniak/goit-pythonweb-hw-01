
from abc import ABC, abstractmethod

from logger import get_logger

logger = get_logger(__name__)



class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def get_books(self) -> list:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> bool:
        for i, b in enumerate(self._books):
            if b.title == title:
                del self._books[i]
                return True
        return False

    def get_books(self) ->list:
        return tuple(self._books)




class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self._library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        self._library.add_book(Book(title=title, author=author, year=year))
        logger.info("Книгу додано: %s — %s (%d)", author, title, year)

    def remove_book(self, title: str) -> None:
        removed = self._library.remove_book(title)
        if removed:
            logger.info("Книгу видалено: %s", title)
        else:
            logger.info("Книгу не знайдено: %s", title)

    def show_books(self) -> None:
        books = self._library.get_books()
        if not books:
            logger.info("Бібліотека порожня.")
            return
        for book in books:
            logger.info("Title: %s, Author: %s, Year: %d", book.title, book.author, book.year)


def main() -> None:
    library = Library()
    manager = LibraryManager(library)
    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()
        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year_raw = input("Enter book year: ").strip()
                try:
                    year = int(year_raw)
                except ValueError:
                    logger.info("Невірний формат року: %s", year_raw)
                    continue
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
