class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self, quantity):
        return self.price * quantity


class Electronics(Item):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty


class Clothing(Item):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size


class Book(Item):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.calculate_price(1)  # Assuming quantity is always 1 for simplicity
        return total_price


# Example usage:

electronics_item = Electronics("Smartphone", 799.99, "1-year warranty")
clothing_item = Clothing("T-shirt", 19.99, "L")
book_item = Book("Python Crash Course", 29.99, "Eric Matthes")

cart = ShoppingCart()
cart.add_item(electronics_item)
cart.add_item(clothing_item)
cart.add_item(book_item)

total_price = cart.calculate_total_price()
print("Total price in the shopping cart:", total_price)