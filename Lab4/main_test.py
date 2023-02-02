import unittest
from main import BusTicket, Ticket  # импортируем то, что будем тестировать


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.owner = 'Natalia Gryaznova'
        cls.price = 100.23
        cls.valid_date = '22-03-2023'
        cls.ticket = Ticket(cls.owner, cls.price, cls.valid_date)

    def test_return_ticket(self):
        print("test_case_return_ticket")    # check class method
        self.assertEqual(self.ticket.TOTAL_TICKETS_NUMBER, 99)
        Ticket.return_ticket()
        self.assertEqual(self.ticket.TOTAL_TICKETS_NUMBER, 100)  # add assertion here

    def test_update_ticket_price(self):
        print("test_case_update_price")     # check self method
        self.ticket.update_price(discount=25)
        self.assertEqual(self.ticket.price, 75.17)

    def test_calc_price(self):
        print("test_case_calc_price")       # check static method
        final_price = Ticket.calc_price(base_price=self.ticket.price,
                                        discount=25)
        self.assertEqual(final_price, 75.17)

    def test_assert_discount_value(self):
        print("test_case_discount_value")   # check static method, negative
        with self.assertRaises(ValueError):
            Ticket.calc_price(base_price=self.ticket.price,
                              discount=-20)

    def test_assert_owner_invalid_type(self):
        print("test_case_owner_invalid_type")   # check owner type, negative
        with self.assertRaises(TypeError):
            self.ticket.owner = 123

    def test_assert_owner_empty(self):
        print("test_case_owner_empty")   # check owner value, negative
        with self.assertRaises(ValueError):
            self.ticket.owner = ''

    def test_assert_owner_long_name(self):
        print("test_case_owner_long_name")   # check owner value, negative
        with self.assertRaises(ValueError):
            self.ticket.owner = '*' * 256

    def test_assert_discount_type(self):
        print("test_case_discount_type")   # check discount type, negative
        with self.assertRaises(TypeError):
            Ticket.calc_price(base_price=self.ticket.price,
                              discount='25')

    def test_assert_owner_value_getter(self):
        print("test_case_owner_value_getter")   # check getter for owner
        self.assertEqual(self.ticket.owner, self.owner)

    def test_assert_price_value_getter(self):
        print("test_case_price_value_getter")   # check getter for price
        self.assertEqual(self.ticket.price, self.price)


class MyTestCaseChild(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("setUp")
        cls.owner = 'Natalia Gryaznova'
        cls.price = 100.23
        cls.valid_date = '22-03-2023'
        cls.driver = None
        cls.ticket = BusTicket(cls.owner, cls.price, cls.valid_date, cls.driver)

    def test_choose_driver(self):
        print("test_case_choose_driver")    # check class method
        self.assertIsNone(self.ticket.driver)
        driver = BusTicket.choose_free_driver()
        self.assertIn(driver, self.ticket.DRIVERS)

    def test_set_driver(self):
        print("test_case_set_driver")    # check setter + getter for driver
        self.assertIsNone(self.ticket.driver)
        self.ticket.driver = "driver_3"
        self.assertEqual(self.ticket.driver, "driver_3")

    def test_assert_driver_long_name(self):
        print("test_case_driver_long_name")   # check owner value, negative
        with self.assertRaises(ValueError):
            self.ticket.driver = '*' * 256


if __name__ == '__main__':
    unittest.main()
