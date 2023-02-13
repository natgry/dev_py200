import unittest
from product import Product  # импортируем то, что будем тестировать


class ProductTestCasePositive(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("setUp")
        cls.name = 'Milk'
        cls.price = 55.90
        cls.rating = 10.93
        cls.product = Product(cls.name, cls.price, cls.rating)
        print(f"Product ID: {cls.product.id}")

    # getter tests
    def test_assert_id_value_getter_multiple_products(self):
        print("test_assert_id_value_getter_multiple_products")
        name = 'Milk2'
        price = 55.90
        rating = 10.93
        product_2 = Product(name, price, rating)
        self.assertIsNotNone(self.product.id)
        self.assertEqual(product_2.id, self.product.id + 1)

    def test_assert_name_value_getter(self):
        print("test_assert_name_value_getter")
        self.assertEqual(self.product.name, self.name)

    def test_assert_price_value_getter(self):
        print("test_assert_price_value_getter")
        self.assertEqual(self.product.price, self.price)

    def test_set_price(self):
        print("test_set_price")
        old_price = self.product.price
        new_price = old_price * 2
        self.product.price = new_price
        self.assertEqual(self.product.price, new_price)
        self.product.price = old_price

    def test_set_rating(self):
        print("test_set_rating")
        old_rating = self.product.rating
        new_rating = old_rating + 0.05
        self.product.rating = new_rating
        self.assertEqual(self.product.rating, new_rating)
        self.product.rating = old_rating

    def test_str_presentation(self):
        print("test_str_presentation")
        str_exp = f"{self.product.id}_{self.product.name}"
        str_act = str(self.product)
        self.assertEqual(str_act, str_exp)

    def test_repr_presentation(self):
        print("test_repr_presentation")
        str_exp = f"Product(name={self.product.name!r}," \
                  f" price={self.product.price!r}, " \
                  f"rating={self.product.rating!r})"
        str_act = repr(self.product)
        self.assertEqual(str_act, str_exp)


class ProductTestCaseNegative(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("setUp")
        cls.name = 'Milk'
        cls.price = 55.90
        cls.rating = 10.93
        cls.product = Product(cls.name, cls.price, cls.rating)
        print(f"Product ID: {cls.product.id}")

    # setter tests
    def test_set_name(self):
        print("test_set_name")
        with self.assertRaises(AttributeError):
            self.product.name = 'new product name'

    def test_set_id(self):
        print("test_set_id")
        with self.assertRaises(AttributeError):
            self.product.id = 1

    def test_set_price_invalid_value(self):
        print("test_set_price_invalid_value")
        with self.assertRaises(ValueError):
            self.product.price = -1.1

    def test_set_price_invalid_type(self):
        print("test_set_price_invalid_type")
        with self.assertRaises(TypeError):
            self.product.price = 10

    def test_set_rating_invalid_value(self):
        print("test_set_rating_invalid_value")
        with self.assertRaises(ValueError):
            self.product.rating = -1.1

    def test_set_rating_invalid_type(self):
        print("test_set_rating_invalid_type")
        with self.assertRaises(TypeError):
            self.product.rating = 10

    # invalid type initialization
    def test_init_name_invalid_type(self):
        print("test_init_name_invalid_type")
        name = 100
        price = 55.90
        rating = 10.93
        with self.assertRaises(TypeError):
            Product(name, price, rating)

    def test_init_price_invalid_type(self):
        print("test_init_price_invalid_type")
        name = 'Milk'
        price = 55
        rating = 10.93
        with self.assertRaises(TypeError):
            Product(name, price, rating)

    def test_init_rating_invalid_type(self):
        print("test_init_price_invalid_type")
        name = 'Milk'
        price = 55.90
        rating = 10
        with self.assertRaises(TypeError):
            Product(name, price, rating)

    # invalid value initialization
    def test_init_name_invalid_value(self):
        print("test_init_name_invalid_value")
        name = ''
        price = 55.90
        rating = 10.93
        with self.assertRaises(ValueError):
            Product(name, price, rating)

    def test_init_price_invalid_value(self):
        print("test_init_price_invalid_value")
        name = 'Milk'
        price = -1.2
        rating = 10.93
        with self.assertRaises(ValueError):
            Product(name, price, rating)

    def test_init_rating_invalid_value(self):
        print("test_init_rating_invalid_value")
        name = 'Milk'
        price = 55.90
        rating = -10.7
        with self.assertRaises(ValueError):
            Product(name, price, rating)


if __name__ == '__main__':
    unittest.main()
