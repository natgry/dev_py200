""" Принцип единой ответственности """


class Duck:

    def __init__(self, name):
        self.__name = name

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Communicator:

    # TODO Подумать нужен ли конструктор для класса и параметры для передачи в класс
    def __init__(self):
        pass
        # конструктор не нужен, объекты для взаимодействия передаются через методы

    # TODO Реализовать класс для взаимодействия двух и БОЛЕЕ уток
    def communicate(self, *duck_list: "Duck"):
        greeting = ''
        for i, duck in enumerate(duck_list):
            greet_list = duck_list[i+1:]
            for who_greet in greet_list:
                greeting += f"{duck.name}: {duck.do_sound()}, hello {who_greet.name}\n" \
                            f"{who_greet.name}: {who_greet.do_sound()}, hello {duck.name}\n"
        return greeting


duck_1 = Duck("Duck_1")
duck_2 = Duck("Duck_2")
duck_3 = Duck("Duck_3")
duck_4 = Duck("Duck_4")

communicator = Communicator()
result = communicator.communicate(duck_1, duck_2, duck_3)
print(result)  # -> "Duck_1 поприветсвовала Duck_2, Duck_2 поприветствовала Duck_1"
