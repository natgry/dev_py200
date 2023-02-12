from cart import Cart
from id_counter import IdCounter
from password import Password

ID = IdCounter()


class User:
    """Класс, в котором хранится информация о пользователе"""
    ID = IdCounter()

    def __init__(self, username, password):
        """
        Создание и подготовка к работе объекта "User"
        :param username: имя пользователя
        :param password: пароль пользователя
        """

        self.__id = ID.id
        self._username = None
        self.__password = Password(password)
        self._cart = Cart()
        self._init_username(username)
        ID.next()

    def _init_username(self, username: str) -> None:
        """
        Инициализация имени пользователя.
        :param username: имя пользователя
        :return: None
        :raise ValueError: Если имя пользователя пустое или превышает 255 символов.
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if len(username) == 0:
            raise ValueError("Имя пользователя должно быть непустой строкой")
        self._username = username

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value):
        raise AttributeError("Значение атрибута 'username' изменить нельзя")

    @property
    def password(self) -> Password:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        self.__password = Password(value)

    @property
    def cart(self) -> Cart:
        return self._cart

    @cart.setter
    def cart(self, value):
        raise AttributeError("Значение атрибута 'cart' изменить нельзя")

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value):
        raise AttributeError("Значение атрибута 'id' изменить нельзя")

    def __str__(self):
        return f"{self.__id}_{self.username}"

    def __repr__(self):
        return f"{self.__class__.__name__}(username={self.username!r}, " \
               f"password=" \
               f"'password1')"


if __name__ == "__main__":
    # test User
    u1 = User("Alex", "asfafaf123333333")
    u2 = User("Sandra", "qwerty12445465656")

    print(u1.id)
    print(u2.id)
    u_list = [u1, u2]
    print(u_list)
    for u in u_list:
        print(u)

