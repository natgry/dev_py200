import doctest
from typing import Union

from book_generator import get_random_book


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
class Book:
    """ Класс, который описывает книгу """

    def __init__(self, id_: int, name: str, pages: int,
                 year: int, isbn13: str, rating: Union[int, float],
                 price: Union[int, float], authors: list):
        """
        Создание и подготовка к работе объекта "Книга"

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        :param year: Год издания книги
        :param isbn13: Международный стандартный книжный номер, ISBN13
        :param rating: Рейтинг книги
        :param price: Стоимость книги
        :param authors: Список авторов книги

        # Примеры:
        # # инициализация экземпляра книги
        # >>> book = Book(id=1, name='Унесённые ветром', pages=561, year=1397, isbn13='978-1-86025-988-3', rating=8.990124180652794, price=59.75087190851305, authors=['Зоя Калинина'])
        # >>> book = Book(id=-1, name='Унесённые ветром', pages=561, year=1397, isbn13='978-1-86025-988-3', rating=8.990124180652794, price=59.75087190851305, authors=['Зоя Калинина'])
        # Traceback (most recent call last):
        # ...
        # ValueError: Идентификатор книги должен быть положительным числом
        # >>> book = Book(id=1, name='', pages=561, year=1397, isbn13='978-1-86025-988-3', rating=8.990124180652794, price=59.75087190851305, authors=['Зоя Калинина'])
        # Traceback (most recent call last):
        # ...
        # ValueError: Название книги должно быть непустой строкой
        # >>> book = Book(id=1, name='Унесённые ветром', pages=0, year=1397, isbn13='978-1-86025-988-3', rating=8.990124180652794, price=59.75087190851305, authors=['Зоя Калинина'])
        # Traceback (most recent call last):
        # ...
        # ValueError: Количество страниц в книге должно быть больше 0
        """
        self.id = None
        self.name = None
        self.pages = None
        self.year = None
        self.isbn13 = None
        self.rating = None
        self.price = None
        self.authors = None
        self.init_id(id_)
        self.init_name(name)
        self.init_pages(pages)
        self.init_year(year)
        self.init_isbn13(isbn13)
        self.init_rating(rating)
        self.init_price(price)
        self.init_authors(authors)

    def init_id(self, id_: int) -> None:
        """
        Инициализация идентификатора книги.

        :param id_: Идентификатор книги.
        :return: None
        :raise ValueError: Если идентификатор меньше 0.
        """
        if not isinstance(id_, int):
            raise TypeError(f"Идентификатор книги должен быть типа {int}")
        if id_ < 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id = id_

    def init_name(self, name: str) -> None:
        """
        Инициализация имени книги.

        :param name: Название книги.
        :return: None
        :raise ValueError: Если название книги является пустой строкой.
        """
        if not isinstance(name, str):
            raise TypeError(f"Название книги должно быть типа {str}")
        if len(name) == 0:
            raise ValueError("Название книги должно быть непустой строкой")
        self.name = name

    def init_pages(self, pages: int) -> None:
        """
        Инициализация количества страниц книги.
        :param pages: На какое значение увеличить стоимость билета.
        :return: None
        :raise ValueError: Если количество страниц не является положительным числом.
        """
        if not isinstance(pages, int):
            raise TypeError(f"Количество страниц в книге должно быть типа {int}")
        if pages < 1:
            raise ValueError("Количество страниц в книге должно быть больше 0")
        self.pages = pages

    def init_year(self, year: int) -> None:
        """
        Инициализация года издания книги.
        :param year: Год издания книги.
        :return: None
        :raise ValueError: Если год издания книги не является положительным числом.
        """
        if not isinstance(year, int):
            raise TypeError(f"Год издания книги должен быть типа {int}")
        if year < 0:
            raise ValueError("Год издания книги должен быть больше 0")
        self.year = year

    def init_isbn13(self, isbn13: str) -> None:
        """
        Инициализация ISBN_13 книги.
        :param isbn13: Название книги.
        :return: None
        :raise ValueError: Если ISBN книги является пустой строкой.
        """
        if not isinstance(isbn13, str):
            raise TypeError(f"ISBN книги должен быть типа {str}")
        if len(isbn13) == 0:
            raise ValueError("ISBN книги должен быть непустой строкой")
        self.isbn13 = isbn13

    def init_rating(self, rating: Union[int, float]) -> None:
        """
        Инициализация рейтинга книги.
        :param rating: Рейтинг книги.
        :return: None
        :raise ValueError: Если рейтинг книги является отрицательным числом.
        """
        if not isinstance(rating, (int, float)):
            raise TypeError(f"Рейтинг книги должен быть типа [{int}, {float}]")
        if rating < 0 or rating < 0.0:
            raise ValueError("Рейтинг книги должен быть больше 0")
        self.rating = rating

    def init_price(self, price: Union[int, float]) -> None:
        """
        Инициализация стоимости книги.
        :param price: Стоимость книги.
        :return: None
        :raise ValueError: Если стоимость книги является отрицательным числом.
        """
        if not isinstance(price, (int, float)):
            raise TypeError(f"Стоимость книги должна быть типа [{int}, {float}]")
        if price < 0 or price < 0.0:
            raise ValueError("Стоимость книги должна быть больше 0")
        self.price = price

    def init_authors(self, authors: list) -> None:
        """
        Инициализация списка авторов книги.
        :param authors: Список авторов книги.
        :return: None
        :raise ValueError: Если список авторов книги является пустым.
        """
        if not isinstance(authors, list):
            raise TypeError(f"Список авторов книги должен быть типа {list}")
        if not authors:
            raise ValueError("Список авторов книги должен быть непустым")
        self.authors = authors

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, name='{self.name}', " \
               f"pages={self.pages}, " \
               f"year={self.year}, " \
               f"isbn13='{self.isbn13}', " \
               f"rating={self.rating}, " \
               f"price={self.price}, " \
               f"authors={self.authors})"

    def __str__(self):
        return f'Книга "{self.name}"'


if __name__ == '__main__':
    #doctest.testmod()  # тестирование примеров, которые находятся в документации

    # инициализируем список книг
    book_count = 50
    book_gen_ = get_random_book(book_count=book_count)
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
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
