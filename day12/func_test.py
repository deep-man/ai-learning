#基本语法
def greet():
    print("你好，欢迎学习Python")

greet()
greet()

#带参数的函数
def greet(name):
    print(f"你好，{name}")

greet("小明")
greet("小红")

#带返回值的函数
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

