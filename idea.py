import doctest


AREAS = ('science', 'business', 'art')


class Patent:
    """ Класс, который описывает патент. """

    def __init__(self, author: str, intro: str, area: str):
        """
        Создание и подготовка к работе объекта "Патент"

        :param author: Автор патента
        :param intro: Описание патента
        :param area: Область применения патента

        Примеры:
        # инициализация экземпляра класса
        >>> patent = Patent('Natalia Gryaznova', 'Some description', 'art')
        >>> patent = Patent('', 'Some description', 'art')
        Traceback (most recent call last):
        ...
        ValueError: Автор патента должен быть непустой строкой
        >>> patent = Patent('Ivan Petrov', '', 'business')
        Traceback (most recent call last):
        ...
        ValueError: Описание патента должно быть не меньше 10 символов
        >>> patent = Patent('Ivan Petrov', 'Some description', 'sport')
        Traceback (most recent call last):
        ...
        ValueError: Область применения патента неизвестна

        """
        self.author = author
        self.intro = intro
        self.area = area
        self.init_author(author)
        self.init_intro(intro)
        self.init_area(area)

    def init_intro(self, intro: str) -> None:
        """
        Инициализация описания патента.
        :param intro: Описание патента
        :return: None
        :raise ValueError: Если описание патента меньше 10 символов или
                            превышает 255 символов.
        """
        if not isinstance(intro, str):
            raise TypeError("Описание патента должно быть типа str")
        if len(intro) > 255:
            raise ValueError("Описание патента должно быть не больше 255 символов")
        if len(intro) < 10:
            raise ValueError("Описание патента должно быть не меньше 10 символов")
        self.intro = intro

    def init_area(self, area: str) -> None:
        """
        Инициализация области применения патента.
        :param area: Область применения патента
        :return: None
        :raise ValueError: Если область применения патента не соотвествует известным областям.
        """
        if not isinstance(area, str):
            raise TypeError("Область применения патента должна быть типа str")
        if area not in AREAS:
            raise ValueError("Область применения патента неизвестна")
        self.area = area

    def init_author(self, author: str) -> None:
        """
        Инициализация автора патента.
        :param author: Автор патента
        :return: None
        :raise ValueError: Если автор патента - пустое значение.
        """
        if not isinstance(author, str):
            raise TypeError("Автор патента должна быть типа str")
        if len(author) == 0:
            raise ValueError("Автор патента должен быть непустой строкой")
        self.author = author

    def change_area(self, area):
        """
        Замена области применения патента на другую область.
        :param area: Область применения патента
        :return:
        :raise ValueError: Если область применения патента не соотвествует известным областям.

        Примеры:
        >>> patent = Patent('Natalia Gryaznova', 'Some description', 'art')
        >>> patent.change_area('business')
        >>> patent.change_area('sport')
        Traceback (most recent call last):
        ...
        ValueError: Область применения патента неизвестна
        """
        if not isinstance(area, str):
            raise TypeError("Область применения патента должна быть типа str")
        if area not in AREAS:
            raise ValueError("Область применения патента неизвестна")
        ...

    def add_intro(self, intro: str) -> None:
        """
        Добавление описания к патенту.
        :param intro: Описание патента
        :return: None
        :raise ValueError: Если описание патента превышает 255 символов.
        Примеры:
        >>> patent = Patent('Natalia Gryaznova', 'Some description', 'art')
        >>> patent.add_intro('Some added description')
        >>> patent.add_intro('Some added description' * 100)
        Traceback (most recent call last):
        ...
        ValueError: Описание патента должно быть не больше 255 символов
        """
        if not isinstance(intro, str):
            raise TypeError("Описание патента должно быть типа str")
        if len(''.join([self.intro, intro])) > 255:
            raise ValueError("Описание патента должно быть не больше 255 символов")
        ...

    def is_art_patent(self) -> bool:
        """
        Функция проверяет, относится ли патент к области искусства.
        :return: Относится ли патент к области искусства

        Примеры:
        >>> patent = Patent('Natalia Gryaznova', 'Some description', 'art')
        >>> patent.is_art_patent()
        >>> patent = Patent('Natalia Gryaznova', 'Some description', 'business')
        >>> patent.is_art_patent()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации