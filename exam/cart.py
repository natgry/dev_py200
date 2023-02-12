from product import Product


class Cart:
    """Класс для корзины, в которой хранится информация о списке товаров"""
    def __init__(self):
        self.cart = []
        self._index = 0

    def add_product(self, product: Product):
        """Добавить продукт в корзину"""
        self.cart.append(product)

    def delete_product(self, product: Product):
        """Удалить продукт из корзины"""
        self.cart = list(filter(lambda x: x.name != product.name, self.cart))

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.cart):
            result = self.cart[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    # test Product
    p1 = Product("Milk", 59.60, 2.2)
    p2 = Product("Water", 34.60, 6.2)
    p3 = Product("Water2", 34.60, 7.2)
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)
    cart.delete_product(p2)
    assert len(cart.cart) == 2
    cart.delete_product(p1)
    assert len(cart.cart) == 1
    cart.delete_product(p3)
    assert len(cart.cart) == 0
