# Переделать классы из Lab 5.3 задания (Bird, Crow, Duck) в соответствии с ISP
# ISP Interface Segregation Principle Принцип разделения интерфейса

from typing import final


class AbstractBird:
    def __init__(self, name):
        self.name = name

    def do_sound(self) -> str:
        pass


class FlyingBird:
    def fly(self):
        pass


class SwimmingBird:
    def swim(self):
        pass


class Crow(AbstractBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def do_sound(self) -> str:
        return "Caw"


class Duck(AbstractBird, SwimmingBird):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"


class AbstractConversation:

    def do_conversation(self) -> list:
        pass


class SimpleConversation(AbstractConversation):

    def __init__(self, bird1: AbstractBird, bird2: AbstractBird):
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
