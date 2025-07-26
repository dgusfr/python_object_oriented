class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

    def __repr__(self):
        return f"MenuItem(name={self.name}, price={self.price})"
