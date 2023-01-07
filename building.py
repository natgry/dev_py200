import doctest


class Building:
    """ Класс, который описывает здание """
    def __init__(self, year: int, capacity: int, renters: list[str]):
        """
        Создание и подготовка к работе объекта "Здание"

        :param year: Год постройки здания
        :param capacity: Количество мест для аренды в здании
        :param renters: Список арендаторов в здании

        Примеры:
        # инициализация экземпляра класса
        >>> building = Building(1967, 3, ['ООО Звезда', 'ООО Графика'])
        >>> building = Building(-1956, 3, ['ООО Звезда'])
        Traceback (most recent call last):
        ...
        ValueError: Год постройки здания должен быть положительным числом
        >>> building = Building(2009, 0, ['ООО Звезда'])
        Traceback (most recent call last):
        ...
        ValueError: Количество мест для аренды должно быть положительным числом
        >>> building = Building(2009, 10, [])
        >>> building = Building(2009, 10, [''])
        Traceback (most recent call last):
        ...
        ValueError: Арендатор должен быть непустой строкой
        """
        self.year = None
        self.capacity = None
        self.renters = None
        self.init_age(year)
        self.init_capacity(capacity)
        self.init_renters(renters)

    def init_age(self, year: int) -> None:
        """
        Инициализация года постройки здания.

        :param year: Год постройки здания.
        :return: None
        :raise ValueError: Если год постройки здания не является положительным числом.
        """
        if not isinstance(year, int):
            raise TypeError("Год постройки здания должен быть типа int")
        if year <= 0:
            raise ValueError("Год постройки здания должен быть положительным числом")
        self.year = year

    def init_capacity(self, capacity: int) -> None:
        """
        Инициализация количества мест для аренды в здании.

        :param capacity: Общее количества мест для аренды в здании.
        :return: None
        :raise ValueError: Если количество мест для аренды не является положительным числом.
        """
        if not isinstance(capacity, int):
            raise TypeError("Количество мест для аренды должно быть типа int")
        if capacity <= 0:
            raise ValueError("Количество мест для аренды должно быть положительным числом")
        self.capacity = capacity

    def init_renters(self, renters: list[str]) -> None:
        """
        Инициализация арендаторов в здании.

        :param renters: Список названий фирм-арендаторов в здании.
        :return: None
        :raise ValueError: Если название арендатора пустая строка или больше 255 символов
        """
        if not isinstance(renters, list):
            raise TypeError("Список арендаторов в здании должно быть типа list")
        for elem in renters:
            if not isinstance(elem, str):
                raise TypeError("Арендатор должен быть типа str")
            if len(elem) == 0:
                raise ValueError("Арендатор должен быть непустой строкой")
            if len(elem) > 255:
                raise ValueError("Арендатор должен быть строкой с длиной до 255")

        self.renters = renters

    def needs_repair(self) -> bool:
        """
        Функция проверяет, требуется ли зданию ремонт.
        :return: Требуется ли зданию ремонт

        Примеры:
        >>> building = Building(2019, 21, ['OOO Графика'])
        >>> building.needs_repair()
        >>> building = Building(1956, 34, ['OOO Графика'])
        >>> building.needs_repair()
        """
        ...

    def add_renter(self, renter: str) -> None:
        """
        Добавление арендатора в здание.
        :param renter: Название фирмы-арендатора
        :raise ValueError: Если название арендатора пустая строка или больше 255 символов.
        Если арендатор уже есть в списке арендаторов.

        Примеры:
        >>> building = Building(2019, 21, ['OOO Графика'])
        >>> building.add_renter('OOO Звезда')
        >>> building.add_renter('OOO Графика')
        Traceback (most recent call last):
        ...
        ValueError: Такой арендатор уже есть в списке арендаторов
        """
        if not isinstance(renter, str):
            raise TypeError("Арендатор должен быть типа str")
        if len(renter) == 0:
            raise ValueError("Арендатор должен быть непустой строкой")
        if len(renter) > 255:
            raise ValueError("Арендатор должен быть строкой с длиной до 255")
        if renter in self.renters:
            raise ValueError("Такой арендатор уже есть в списке арендаторов")
        ...

    def is_renter(self, renter: str) -> bool:
        """
        Проверяет, занимает ли данный арендатор место в здании.
        :return: Занимает ли данный арендатор место в здании

        Примеры:
        >>> building = Building(2019, 21, ['OOO Графика'])
        >>> building.is_renter('OOO Графика')
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
