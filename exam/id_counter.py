class IdCounter:
    """ Класс, в котором хранится генератор значений id
    (обычный инкремент на 1). """

    def __init__(self):
        """
        Создание и подготовка к работе объекта "IdCounter
        :param __id: Счетчик, инкремент на 1
        """
        self.__id = None
        self.__init_id()

    def __init_id(self):
        """
        Инициализация генератора значений.
        :return: None
        """
        self.__id = 0

    @property
    def id(self) -> int:
        return self.__id

    def next(self) -> int:
        """
        Генерируем следующее значение.
        :return: значение ID, увеличенное на 1
        """
        self.__id += 1
        return self.__id

    @id.setter
    def id(self, value):
        raise AttributeError("Значение атрибута 'id' изменить нельзя")


if __name__ == "__main__":
    # test IdCounter
    c = IdCounter()
    print(c.id)
    print(c.next())
    print(c.id)
