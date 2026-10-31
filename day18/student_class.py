class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def total(self):
        return self.chinese + self.math + self.english

    def avg(self):
        return self.total() / 3

    def show(self):
        print(f"{self.name}:总分{self.total()},平均分{self.avg():.2f}")


s1 = Student("小明", 90, 98, 90)
s2 = Student("小黄", 90, 88, 76)
s3 = Student("小蓝", 98, 87, 67)

s1.show()
print(s1.total())