class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError(f"Название книги должно быть типа {str}")
        if not isinstance(author, str):
            raise TypeError(f"Автор книги должен быть типа {str}")
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        raise AttributeError(f"Значение атрибута {self.__name} изменить нельзя")

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        raise AttributeError(f"Значение атрибута {self.__author} изменить нельзя")

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    """ Класс бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        if not isinstance(pages, int):
            raise TypeError(f"Количество страниц должно быть типа {int}")
        if pages < 0:
            raise ValueError(f"Количество страниц не может быть отрицательным числом")
        self.__pages = pages

        super(PaperBook, self).__init__(name, author)

    def __str__(self):
        return f"{super(PaperBook, self).__str__()}. Количество страниц {self.__pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"Количество страниц должно быть типа {int}")
        if value < 0:
            raise ValueError(f"Количество страниц не может быть отрицательным числом")
        else:
            self.__pages = value


class AudioBook(Book):
    """ Класс аудио книги. """
    def __init__(self, name: str, author: str, duration: float):
        if not isinstance(duration, float):
            raise TypeError(f"Продолжительность книги должна быть типа {float}")
        if duration < 0.0:
            raise ValueError(f"Продолжительность книги не может быть отрицательным числом")
        else:
            self.__duration = duration
            
        super(AudioBook, self).__init__(name, author)

    def __str__(self):
        return f"{super(AudioBook, self).__str__()}. Продолжительность книги {self.__duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"(name={self.name!r}, author={self.author!r}, duration={self.__duration!r})"

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, float):
            raise TypeError(f"Продолжительность книги должна быть типа {float}")
        if value < 0.0:
            raise ValueError(f"Продолжительность книги не может быть отрицательным числом")
        else:
            self.__duration = value


if __name__ == '__main__':
    book = Book('test_name', 'test_author')
    print(book)
    print([book])
    print(book.name)
    print(book.author)

    book_paper = PaperBook('test_name', 'test_author', 8)
    print(book_paper)
    print([book_paper])
    book_audio = AudioBook('test_name', 'test_author', 32.33)
    print(book_audio)
    print([book_audio])

