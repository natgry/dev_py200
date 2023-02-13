import re

import hashlib


class Password:
    """Класс, который ответственен за выдачу хэш-значения пароля
    и проверке пароля с его хэш значением
    """

    def __init__(self, password: str):
        """
        Создание и подготовка к работе объекта "Password
        :param password: Пароль
        """

        self._password = None
        self._init_psw(password)

    def _init_psw(self, value: str) -> None:
        """
        Инициализация пароля.
        :param password: Пароль
        :return: None
        """
        self.validate_password(value)
        self._password = value

    @staticmethod
    def validate_password(password: str) -> None:
        """
        Проверка формата пароля.
        :param password: Пароль для проверки
        :return: None
        :raise: ValueError: Если пароль не соответствует требованиям.
                TypeError: Если пароль не является строкой
        """
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть типа str")
        if len(password) < 8:
            raise ValueError("Пароль должен состоять минимум из 8 символов")
        if not (re.findall(r'[a-zA-Z]+', password)
                and re.findall(r'\d+', password)):
            raise ValueError("Пароль должен включать как цифры так и буквы")

    @staticmethod
    def get(password: str) -> str:
        """
        Выдаёт хэш-значение для переданного пароля.
        :param password: Пароль
        :return: Хэш-значение для переданного пароля
        """
        Password.validate_password(password)
        hash_psw = hashlib.sha256(password.encode()).hexdigest()
        return hash_psw

    @staticmethod
    def check(password: str, password_hash: str) -> bool:
        """
        Проверяет, соотносится ли передаваемый пароль с его хэш-значением.
        :param password: Пароль
        :param password_hash: Хэш-значение для переданного пароля
        :return: True/False - cоотносится ли передаваемый пароль с его хэш-значением
        """
        return Password.get(password) == password_hash

    @property
    def password(self):
        return "password1"

    @password.setter
    def password(self, value):
        self.validate_password(value)
        self._password = value


if __name__ == "__main__":
    # test Password
    p = Password("1234e56789q@")
    h = p.get(p.password)
    print(h)
    print(p.check(p.password, h))

