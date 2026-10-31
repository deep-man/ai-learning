#类把“数据”和“行为”放在一起

#创建对象
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def total(self):
        return self.chinese + self.math + self.english

#学生对象自带total()方法，不用外部函数

# 要点：
# class 是关键字，类名建议首字母大写
# __init__ 是构造方法，创建对象时自动调用
# self 代表对象自己，必须是第一个参数
# self.属性 是对象的属性
# 方法第一个参数必须是 self
    def avg(self):
        return self.total() / 3

    def show(self):
        print(f"{self.name}:总分{self.total()},平均分{self.avg():.2f}")
s1 = Student("小明", 85, 92, 78)
s2 = Student("小红", 90, 88, 95)

s1.show()
s2.show()

print(s1.total())
print(s2.avg())

#Studnet(...)调用时。自动执行__init__，不需要手动调用

#self是什么
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"我是{self.name}")

# s1 = Student("小明")
# s2 = Student("小红")

# s1.greet()
# s2.greet()
#self.name取的是“当前对象”的name

#属性可以修改
s1 = Student("小明", 85, 92, 78)
print(s1.chinese)

s1.chinese = 95
print(s1.chinese)
print(s1.total)