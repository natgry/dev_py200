# Принцип открытости/закрытости
from typing import Any


class Duck:

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return f"{self.name}: Quack"


class Communicator:
    def __init__(self):
        pass

    def communicate(self, *duck_list: "Duck"):
        greeting = ''
        for i, duck in enumerate(duck_list):
            greet_list = duck_list[i+1:]
            for who_greet in greet_list:
                greeting += f"{duck.do_sound()}, hello {who_greet.name}\n" \
                            f"{who_greet.do_sound()}, hello {duck.name}\n"
        return greeting


class Specification:
    def is_satisfied(self, item: Any):
        pass


class Filter:
    def filter(self, items: list, spec: Specification):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item: Any):
        return item.color == self.color


# TODO Реализовать класс SizeSpecification
class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item: Any):
        return item.size == self.size


class ColorFilter(Filter):
    def filter(self, items: Any, spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


# TODO Реализовать класс SizeFilter
class SizeFilter(Filter):
    def filter(self, items: Any, spec: Specification):
        for item in items:
            if spec.is_satisfied(item):
                yield item


duck_1 = Duck("Duck_1", "GREEN", "BIG")
duck_2 = Duck("Duck_2", "BROWN", "SMALL")
duck_3 = Duck("Duck_3", "GREEN", "MEDIUM")
duck_4 = Duck("Duck_4", "BLUE", "BIG")

ducks = [duck_1, duck_2, duck_3, duck_4]

cf = ColorFilter()
cs = ColorSpecification("GREEN")
for p in cf.filter(ducks, cs):
    print(f"{p.name} is green")

# TODO Отсортировать уток по размеру BIG
sf = SizeFilter()
ss = SizeSpecification("BIG")
for p in sf.filter(ducks, ss):
    print(f"{p.name} is big")


