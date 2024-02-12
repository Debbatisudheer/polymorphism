# Duck typing - no explicit type checking
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total_price(self):
        self.total_price = sum(item.calculate_total_price() for item in self.items if not isinstance(item, Coupon))
        return self.total_price

    def calculate_individual_prices(self):
        individual_prices = [(item.name, item.calculate_total_price()) for item in self.items if not isinstance(item, Coupon)]
        return individual_prices

# Superclass and Subclasses
class Electronics:
    def __init__(self, name, price, warranty):
        self.name = name
        self.price = price
        self.warranty = warranty

    def calculate_total_price(self):
        return self.price


class Clothing:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def calculate_total_price(self):
        return self.price


# Method Overriding
class Book:
    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author

    def calculate_total_price(self):
        return self.price


# Polymorphism
class GiftCard:
    def __init__(self, name, amount):
        self.name = name
        self.price = amount

    def calculate_total_price(self):
        return self.price  # Gift card has fixed value, regardless of quantity


# Dynamic typing
class SpecialOffer:
    def __init__(self, discount):
        self.discount = discount

    def apply_discount(self, price):
        return price * (1 - self.discount)


# Magic Methods
class Coupon:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def __str__(self):
        return f"{self.name} - {self.discount}% off"

# Interface
class Delivery:
    def deliver(self):
        pass


class HomeDelivery(Delivery):
    def deliver(self):
        print("Delivering to home address.")


class StorePickup(Delivery):
    def deliver(self):
        print("Ready for store pickup.")


# Multiple Level Inheritance
class FastDelivery(HomeDelivery):
    def deliver(self):
        super().deliver()
        print("Fast delivery service.")


# Meta Programming
def apply_discount_to_shopping_cart(shopping_cart, discount):
    shopping_cart.total_price = discount.apply_discount(shopping_cart.total_price)
    return shopping_cart


# Example usage
electronics = Electronics("Laptop", 1200, "1-year warranty")
clothing = Clothing("T-shirt", 25, "M")
book = Book("Python Cookbook", 35, "John Doe")
gift_card = GiftCard("Amazon Gift Card", 50)
coupon = Coupon("25% Off Coupon", 25)
special_offer = SpecialOffer(0.1)  # 10% discount

cart = ShoppingCart()
cart.add_item(electronics)
cart.add_item(clothing)
cart.add_item(book)
cart.add_item(gift_card)
cart.add_item(coupon)

print("Individual prices before discount:")
for name, price in cart.calculate_individual_prices():
    print(f"{name}: ${price}")

cart.calculate_total_price()
print("Total price before discount:", cart.total_price)

cart = apply_discount_to_shopping_cart(cart, special_offer)
print("Total price after discount:", cart.total_price)

# Polymorphic Delivery
home_delivery = HomeDelivery()
store_pickup = StorePickup()
fast_delivery = FastDelivery()

home_delivery.deliver()
store_pickup.deliver()
fast_delivery.deliver()