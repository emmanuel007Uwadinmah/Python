#item1 = "Phone"
#item1_price = 100
#item1_quantity = 5
#item1_price_total = item1_price * item1_quantity

class Item:
    def __init__(self, name: str, price: float, quantity=0, color = Null):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.color = color
        print(f"{name} was created!")
    def calc_total_price(self):
        return self.price * self.quantity
    
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3, "black")

print(item1.calc_total_price())
print(item2.calc_total_price())

print(item1.color())
print(item2.color())


