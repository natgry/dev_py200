# Принцип подстановки Лискова

from abc import ABC, abstractmethod
from typing import final


class Bird(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def do_sound(self) -> str:
        pass


class Crow(Bird):

    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def swim(self):
        raise NotImplementedError("Crows don't swim!")

    def do_sound(self) -> str:
        return "Caw"


class Duck(Bird):

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"


class AbstractConversation:

    def do_conversation(self) -> list:
        pass


# TODO Переделать класс для возможности передачи в него всех объектов типа Птица
class SimpleConversation(AbstractConversation):

    def __init__(self, bird1: Bird, bird2: Bird):
        self.bird1 = bird1
        self.bird2 = bird2

    def do_conversation(self) -> list:
        sentence1 = f"{self.bird1.name}: {self.bird1.do_sound()}, hello {self.bird2.name}"
        sentence2 = f"{self.bird2.name}: {self.bird2.do_sound()}, hello {self.bird1.name}"
        return [sentence1, sentence2]


class Communicator:

    def __init__(self, channel):
        self.channel = channel

    @final
    def communicate(self, conversation: AbstractConversation):
        print(*conversation.do_conversation(),
              f"(via {self.channel})",
              sep='\n')


birds = [Crow('crowFirst'), Duck('duckFirst')]

for bird in birds:
    print(bird.do_sound())

simple_conversation = SimpleConversation(Crow('crowFirst'), Duck('duckFirst'))
print(simple_conversation.do_conversation())

communicator = Communicator(channel='channelX')
communicator.communicate(simple_conversation)
