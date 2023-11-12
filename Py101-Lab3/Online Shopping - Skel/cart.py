class Cart:
    def __init__(self):
        self.list_cart = []

    def add(self, new_product):
        self.list_cart.append(new_product)



    def remove(self, product_name):
        for i in self.list_cart:
            if i.name == product_name:
                self.list_cart.remove(i)


    def view(self):
        return self.list_cart

    def cart_checkout(self):
        x = 0
        for i in self.list_cart:
            x += i.price
        return x