class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price