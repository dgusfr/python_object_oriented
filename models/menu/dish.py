from models.menu.item_menu import MenuItem


class Dish(MenuItem):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description
