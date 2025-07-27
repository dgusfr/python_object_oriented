from models.menu.item_menu import MenuItem


class Drink(MenuItem):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)
        self.type = "Bebida"

    def __str__(self):
        return self.nome
