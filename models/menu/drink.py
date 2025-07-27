from models.menu.item_menu import MenuItem


class Drink(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = "Bebida"

    def __str__(self):
        return self.name
