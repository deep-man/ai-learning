class Product:
    def __init__(self, name, cost, num):
        self.name = name
        self.cost = cost
        self.num = num

    def subtotal(self):
        return self.cost * self.num

class Cart:
    def __init__(self):
        self.products = []
    
    def add(self, product):
        self.products.append(product)

    def total(self):
        total = 0
        for item in self.products:
            total += item.subtotal()
        return total

    def show(self):
        for item in self.products:
            print(f"{item.name}：{item.cost}×{item.num}={item.subtotal()}")
        print(f"总价:{self.total()}")

cart = Cart()
cart.add(Product("苹果", 5, 3))
cart.add(Product("香蕉", 3, 5))
cart.add(Product("橙子", 4, 2))

cart.show()