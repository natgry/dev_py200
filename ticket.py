import doctest


class Ticket:
    """ Класс, который описывает билет. """
    def __init__(self, owner: str, price: float, valid_before: str):
        """
        Создание и подготовка к работе объекта "Билет"

        :param owner: Имя владельца билета
        :param price: Стоимость билета
        :param valid_before: Срок действия билета

        Примеры:
        # инициализация экземпляра класса
        >>> ticket = Ticket('Natalia Gryaznova', 100.99, '22-03-2023')
        >>> ticket = Ticket('Natalia Gryaznova' * 100, 100.99, '22-03-2023')
        Traceback (most recent call last):
        ...
        ValueError: Имя владельца билета должно быть строкой с длиной до 255
        >>> ticket = Ticket('Natalia Gryaznova', -100.99, '22-03-2023')
        Traceback (most recent call last):
        ...
        ValueError: Стоимость билета должна быть большое 0
        >>> ticket = Ticket('Natalia Gryaznova', 100.99, '')
        Traceback (most recent call last):
        ...
        ValueError: Срок действия билета должен быть непустой строкой
        """
        self.owner = None
        self.price = None
        self.valid_before = None
        self.init_owner(owner)
        self.init_price(price)
        self.init_valid_date(valid_before)

    def init_owner(self, owner: str) -> None:
        """
        Инициализация имени владельца билета.
        :param owner: Имя владельца билета
        :return: None
        :raise ValueError: Если имя владельца пустое или превышает 255 символов.

        """
        if not isinstance(owner, str):
            raise TypeError("Имя владельца билета должен быть типа str")
        if len(owner) == 0:
            raise ValueError("Имя владельца билета должно быть непустой строкой")
        if len(owner) > 255:
            raise ValueError("Имя владельца билета должно быть строкой с длиной до 255")
        ...

    def init_price(self, price: float) -> None:
        """
        Инициализация стоимости билета.
        :param price: Стоимость билета
        :return: None
        :raise ValueError: Если значение не является положительным числом.

        """
        if not isinstance(price, float):
            raise TypeError("Стоимость билета должна быть типа float")
        if price <= 0.0:
            raise ValueError("Стоимость билета должна быть большое 0")
        ...

    def init_valid_date(self, valid_before) -> None:
        """
        Инициализация срока действия билета.
        :param valid_before: Срок действия билета
        :return: None
        :raise ValueError: Если срок действия билета является пустой строкой.

        """
        if not isinstance(valid_before, str):
            raise TypeError("Срок действия билета должен быть типа str")
        if len(valid_before) == 0:
            raise ValueError("Срок действия билета должен быть непустой строкой")
        ...

    def change_owner(self, new_owner: str) -> None:
        """
        Поменять владельца билета.
        :param new_owner: Имя нового владельца билета.
        :return: None
        :raise ValueError: Если имя владельца пустое или превышает 255 символов.

        Примеры:
        >>> ticket = Ticket('Natalia Gryaznova', 100.23, '22-03-2023')
        >>> ticket.change_owner('Oleg Ivanov')
        >>> ticket.change_owner('')
        Traceback (most recent call last):
        ...
        ValueError: Имя владельца билета должно быть непустой строкой
        """
        if not isinstance(new_owner, str):
            raise TypeError("Имя владельца билета должен быть типа str")
        if len(new_owner) == 0:
            raise ValueError("Имя владельца билета должно быть непустой строкой")
        if len(new_owner) > 255:
            raise ValueError("Имя владельца билета должно быть строкой с длиной до 255")
        ...

    def raise_price(self, value: float) -> None:
        """
        Увеличение стоимости билета.
        :param value: На какое значение увеличить стоимость билета.
        :return: None
        :raise ValueError: Если значение не является положительным числом.

        Примеры:
        >>> ticket = Ticket('Natalia Gryaznova', 100.23, '22-03-2023')
        >>> ticket.raise_price(25.25)
        >>> ticket.raise_price(-10.0)
        Traceback (most recent call last):
        ...
        ValueError: Величина увеличения стоимости билета должна быть большое 0
        """
        if not isinstance(value, float):
            raise TypeError("Величина увеличения стоимости билета должна быть типа float")
        if value <= 0.0:
            raise ValueError("Величина увеличения стоимости билета должна быть большое 0")
        ...

    def return_ticket(self) -> None:
        """
        Сдать билет в кассу.
        :return: None

        Примеры:
        >>> ticket = Ticket('Natalia Gryaznova', 100.23, '22-03-2023')
        >>> ticket.return_ticket()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации