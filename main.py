from book import Book
from book_generator import get_random_book
from typing import Any

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book


# TODO написать класс Library
class Library:
    """ Класс, который описывает библиотеку """

    def __init__(self, books: list[Book] = None):
        """
        Создание и подготовка к работе объекта "Библиотека"

        :param books: Список книг для добавления в библиотеку. Optional
        """
        self.books = None
        self.init_books(books)

    def init_books(self, books: list[Book]) -> None:
        """
        Инициализация списка книг в библиотеке.

        :param books: Список книг для добавления в библиотеку
        :return: None
        """
        if books is None:
            self.books = []
        else:
            self.books = books.copy()

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        Если книг в библиотеке нет, то вернуть 1.
        Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.
        :return: идентификатор для добавления новой книги в библиотеку
        """
        if not self.books:
            next_book_id = 1
        else:
            last_book_id = self.books[len(self) - 1].id
            next_book_id = last_book_id + 1
        return next_book_id

    def get_index_by_book_id(self, id_: int) -> int:
        """
        Метод, возвращающий индекс книги в списке,
        который хранится в атрибуте экземпляра класса.
        Если книга существует, то вернуть индекс из списка.
        Если книги нет, то вызвать ошибку ValueError с сообщением:
        "Книги с запрашиваемым id не существует"
        :param id_: Идентификатор книги
        :return: Индекс книги в списке
        :raise ValueError: Если книги нет.
        """
        found_index = [index for index, book_ in enumerate(self.books) if book_.id == id_]
        if not found_index:
            raise ValueError(f"Книги с запрашиваемым id={id_} не существует")
        else:
            return found_index[0]

    def __len__(self):
        return len(self.books)


if __name__ == '__main__':
    book_count = 50
    book_gen_ = get_random_book(book_count=50, start_id_=1)
    books_database = []
    for i in range(book_count):
        book = next(book_gen_)
        books_database.append(book)

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"],
             year=book_dict["year"], isbn13=book_dict["isbn13"],
             rating=book_dict["rating"], price=book_dict["price"],
             authors=book_dict["authors"])
        for book_dict in books_database
    ]
    print([book for book in list_books])

    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    print(library_with_books.get_index_by_book_id(60))  # проверяем индекс книги с id, которого не существует
