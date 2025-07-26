class Dish:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} - {self.description}"

    def __repr__(self):
        return f"Dish(name={self.name}, price={self.price}, description={self.description})"
