from random import choice
from typing import Union


class Ticket:
    """ Класс, который описывает билет. """

    TOTAL_TICKETS_NUMBER = 100

    def __init__(self, owner: str, price: float, valid_before: str):
        """
        Создание и подготовка к работе объекта "Билет"
        :param owner: Имя владельца билета
        :param price: Стоимость билета
        :param valid_before: Срок действия билета
        """
        self.__owner = None
        self.__price = None
        self.__valid_before = None
        self._init_owner(owner)
        self._init_price(price)
        self._init_valid_date(valid_before)

        Ticket.TOTAL_TICKETS_NUMBER -= 1

    def _init_owner(self, owner: str) -> None:
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
        self.__owner = owner

    def _init_price(self, price: float) -> None:
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
        self.__price = price

    def _init_valid_date(self, valid_before: str) -> None:
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
        self.__valid_before = valid_before

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self._init_owner(value)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self._init_price(value)

    @property
    def valid_before(self):
        return self.__valid_before

    @valid_before.setter
    def valid_before(self, value):
        self._init_valid_date(value)

    def update_price(self, discount: int) -> None:
        """
        Изменение стоимости билета в зависимости от скидки.
        :param discount: Скидка на билет.
        :return: None
        :raise ValueError: Если значение скидки не является положительным числом.
        """
        if not isinstance(discount, int):
            raise TypeError("Величина скидки должна быть типа int")
        if discount <= 0:
            raise ValueError("Величина скидки должна быть больше положительным числом")
        self.__price = self.calc_price(self.__price, discount)

    @staticmethod
    def calc_price(base_price: float, discount: int = 0):
        if not isinstance(discount, int):
            raise TypeError("Величина скидки должна быть типа int")
        if discount <= 0:
            raise ValueError("Величина скидки должна быть больше положительным числом")

        final_price = base_price - base_price * round(discount / 100, 2)
        return round(final_price, 2)

    @classmethod
    def return_ticket(cls) -> None:
        """
        Сдать билет в кассу.
        :return: None
        """
        cls.TOTAL_TICKETS_NUMBER += 1

    def __str__(self):
        return f"Билет. Владелец {self.__owner}. Стоимость {self.__price}. " \
               f"Срок действия {self.__valid_before}"

    def __repr__(self):
        return f"{self.__class__.__name__}(owner={self.__owner!r}, price={self.__price!r}, " \
               f"valid_before={self.__valid_before!r})"


class BusTicket(Ticket):
    DRIVERS = ["driver_1", "driver_2"]

    """ Класс, который описывает автобусный билет. """
    def __init__(self, owner: str, price: float, valid_before: str, driver: str):
        self.__driver = None
        self._init_driver(driver)
        super(BusTicket, self).__init__(owner, price, valid_before)

    def _init_driver(self, driver: Union[str, None]) -> None:
        """
        Инициализация имени водителя.
        :param driver: Имя водителя
        :return: None
        :raise ValueError: Если имя водителя пустое или превышает 255 символов.
        """
        if driver is not None:
            if not isinstance(driver, str):
                raise TypeError("Имя водителя должен быть типа str")
            if len(driver) == 0:
                raise ValueError("Имя водителя должно быть непустой строкой")
            if len(driver) > 255:
                raise ValueError("Имя водителя должно быть строкой с длиной до 255")
            self.__driver = driver

    def __str__(self):
        return f"{super(BusTicket, self).__str__()}. Водитель {self.__driver}"

    def __repr__(self):
        return f"{self.__class__.__name__}(owner={self.owner!r}, price={self.price!r}, " \
               f"valid_before={self.valid_before!r}, driver={self.driver!r})"

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, value):
        self._init_driver(value)

    @classmethod
    def choose_free_driver(cls):
        return choice(cls.DRIVERS)


if __name__ == "__main__":
    ...
    ticket = Ticket('Natalia Gryaznova', 100.23, '22-03-2023')
    tickets = [ticket]
    print([ticket for ticket in tickets])
    print(ticket)

    ticket_bus = BusTicket('Natalia Gryaznova', 100.23, '22-03-2023', 'driver_1')
    tickets = [ticket_bus]
    print([ticket for ticket in tickets])
    print(ticket_bus)
