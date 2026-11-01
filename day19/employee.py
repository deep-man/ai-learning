class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def show(self):
        print(f"姓名:{self.name},基本工资:{self.base_pay}")

    def salary(self):
        return self.base_pay

class Manager(Employee):
    def __init__(self, name, base_pay, bonus):
        super().__init__(name, base_pay)
        self.bonus = bonus

    def salary(self):
        return self.base_pay + self.bonus

    def show(self):
        print(f"姓名:{self.name},基本工资:{self.base_pay},奖金:{self.bonus}")

class Sales(Employee):
    def __init__(self, name, base_pay, commission):
        super().__init__(name, base_pay)
        self.commission = commission

    def salary(self):
            return self.base_pay + self.commission
    
    def show(self):
            print(f"姓名:{self.name},基本工资:{self.base_pay},提成:{self.commission}")

s1 = Employee("普通员工",3500)
s2 = Manager("经理", 6000, 600)
s3 = Sales("销售", 4000, 4000)
s1.show()
s2.show()
s3.show()
print(f"{s1.name}的工资：{s1.salary()}")
print(f"{s2.name}的工资：{s2.salary()}")
print(f"{s3.name}的工资：{s3.salary()}")

total = s1.salary()+s2.salary()+s3.salary()
print(f"三个人的工资总和是：{total}")