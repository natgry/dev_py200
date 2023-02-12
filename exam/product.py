from id_counter import IdCounter

ID = IdCounter()


class Product:
    """Класс, в котором хранится информация о продукте"""
    def __init__(self, name: str, price: float, rating: float):
        """
        Создание и подготовка к работе объекта "Product
        :param name: название продукта
        :param price: стоимость продукта
        :param rating: рейтинг продукта
        """
        self.__id = ID.id
        self.__name = None
        self.__price = None
        self.__rating = None
        self._init_name(name)
        self._init_price(price)
        self._init_rating(rating)
        ID.next()

    def _init_name(self, name: str) -> None:
        """
        Инициализация названия продукта.
        :param name: название продукта
        :return: None
        :raise ValueError: Если название продукта пустое или превышает 255 символов.
        """
        if not isinstance(name, str):
            raise TypeError("Название продукта должен быть типа str")
        if len(name) == 0:
            raise ValueError("Название продукта должно быть непустой строкой")
        self.__name = name

    def _init_price(self, price: float) -> None:
        """
        Инициализация стоимости товара.
        :param price: Стоимость товара
        :return: None
        :raise ValueError: Если значение не является положительным числом.
        """
        if not isinstance(price, float):
            raise TypeError("Стоимость товара должна быть типа float")
        if price <= 0.0:
            raise ValueError("Стоимость товара должна быть большое 0")
        self.price = price

    def _init_rating(self, rating: float) -> None:
        """
        Инициализация рейтинга книги.
        :param price: рейтинг книги
        :return: None
        :raise ValueError: Если рейтинг не является положительным числом.
        """
        if not isinstance(rating, float):
            raise TypeError("Рейтинг книги доложен быть типа float")
        if rating <= 0.0:
            raise ValueError("Рейтинг книги должен быть большое 0")
        self.rating = rating

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value):
        raise AttributeError("Значение атрибута 'name' изменить нельзя")

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value):
        raise AttributeError("Значение атрибута 'id' изменить нельзя")

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("Стоимость товара должна быть типа float")
        if value <= 0.0:
            raise ValueError("Стоимость товара должна быть большое 0")
        self.__price = value

    @property
    def rating(self) -> float:
        return self.__rating

    @rating.setter
    def rating(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("Рейтинг книги доложен быть типа float")
        if value <= 0.0:
            raise ValueError("Рейтинг книги должен быть большое 0")
        self.__rating = value

    def __str__(self):
        return f"{self.__id}_{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}," \
               f" price={self.price!r}, " \
               f"rating={self.rating!r})"


if __name__ == "__main__":
    # test Product
    p1 = Product("Milk", 59.60, 2.2)
    p2 = Product("Water", 34.60, 6.2)
    p3 = Product("Water2", 34.60, 7.2)

    print(p1.id)
    print(p2.id)
    print(p3.id)
    p_list = [p1, p2, p3]
    print(p_list)
    for p in p_list:
        print(p)
