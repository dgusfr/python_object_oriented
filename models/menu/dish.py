from models.menu.item_menu import MenuItem


class Dish(MenuItem):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        return self.nome

    def apply_discount(self):
        self._price -= self.price * 0.3
