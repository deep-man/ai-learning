class Order():
    total_orders = 0

    def __init__(self, order_num, money):
        self.order_num = order_num
        self.money = money
        Order.total_orders += 1

    def show(self):
        print(f"订单号:{self.order_num},金额:{self.money}")

    def final_amount(self):
        return self.money

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

class DiscountOrder(Order):
    def __init__(self, order_num, money, discount):
        super().__init__(order_num, money)
        self.discount = discount

    def final_amount(self):
        return self.money * self.discount

class VipOrder(Order):
    def __init__(self, order_num, money, integral):
        super().__init__(order_num, money)
        self.integral = integral

    def final_amount(self):
        if (self.money - self.integral) > 0:
            return self.money - self.integral
        else:
            print("折扣金额有误")
            return 0

# d1 = Order('011001',800)
# d1.show()
# d1.final_amount()
# d2 = Order('011002',9000)
# d2.show()
d1 = Order('011001',800)
d2 = Order('011002',8900)
d3 = DiscountOrder('011001',800,0.9)
d4 = VipOrder('011001',800,90)

for order in [d1, d2, d3, d4]:
    order.show()
    print(f"实付：{order.final_amount()}")

print(f"订单总数：{Order.total_orders}")
print(Order.is_valid_amount(0))
print(Order.is_valid_amount(100))