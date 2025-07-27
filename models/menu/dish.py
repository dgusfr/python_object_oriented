from models.menu.item_menu import MenuItem


class Dish(MenuItem):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        return self.nome

    @property
    def price(self):
        return self._price

    def aplly_discount(self):
        self._price -= self._price * 0.03
