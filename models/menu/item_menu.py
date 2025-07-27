from abc import ABC, abstractmethod


class MenuItem(ABC):
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @abstractmethod
    def aplly_discount(self, discount):
        pass
