#默认参数
def greet(name = "同学"):
    print(f"你好,{name}")

greet()
greet("小明")

#关键字参数
def introduce(name, age):
    print(f"我叫{name}, 今年{age}岁")

introduce(age = 20, name = "小明")

#多返回值
def get_min_max(nums):
    return min(nums), max(nums)

low, high = get_min_max([3, 7, 2, 9, 5])
print(low, high)
#return a, b返回的是一个元组(a, b)