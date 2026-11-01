# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"{self.name},{self.age}岁")

# s1 = Student("程宏建", 98)
# s1.show()

#继承：子类自动拥有父类的属性和方法，只写新增的部分
#基本语法
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name},{self.age}岁")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)#子类__init__里先super().__init__(name, age),把公共属性交给父类处理，再写自己新增的属性
        self.grade = grade

    def show(self):
        super().show()
        print(f"年级：{self.grade}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

s = Student("小明", 18, "高三")
t = Teacher("李老师", 35, "数学")

s.show()
t.show()
# 语法                         作用
# class Student(Person):      Student继承Person
# super().__init__(...)       调用父类的__init__
# super().show()              调用父类的show
# 子类重写同名方法              覆盖父类方法
# 子类不写__init__             自动继承父类的__init__
