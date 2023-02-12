from faker_store import product_gen
from user import User


class Store:
    """Класс, который описывает магазин"""
    def __init__(self):
        """
        Создание и подготовка к работе объекта " Магазин"
        """
        self.user = None
        login = psw = None
        login, psw = self.user_auth()
        self.user = User(login, psw)

    def user_auth(self) -> tuple:
        """
        Аутентификация пользователя через консоль:
        логин и пароль будут вводиться через консоль.
        :return: tuple of login and password
        """
        login = input("Введите логин пользователя:\n ")
        psw = input("Введите пароль пользователя:\n ")
        return login, psw

    def add_product(self, product_count) -> None:
        """
        Добавить случайный продукт в корзину пользователя
        :param product_count: количество добавляемых продуктов
        :return: None
        """
        p_gen_ = product_gen(product_count=product_count)
        for _ in range(product_count):
            product = next(p_gen_)
            self.user.cart.add_product(product)

    def print_cart(self) -> None:
        """Пролистать корзину пользователя"""
        for entry in self.user.cart:
            print(entry)


if __name__ == "__main__":
    # test Store
    s = Store()
    s.add_product(10)
    print("==========================")
    print(f"User '{s.user}' cart:")
    print("==========================")
    s.print_cart()

    print("==========================")
    print(f"User '{s.user}' password: {s.user.password.password}")
