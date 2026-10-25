# age = int(input("年龄："))
# print(age)

#异常处理
try:
    age = int(input("年龄："))
    print(f"今年{age}岁")
except ValueError:
    print("输入的不是数字")
# 异常	         什么时候出现
# ValueError	类型转换失败，如 int("abc")
# KeyError	    字典键不存在
# IndexError	列表索引越界
# ZeroDivisionError	除以 0
# TypeError	    类型不匹配

try:
    print("执行")
except:
    print("出错了")
finally:
    print("无论如何都执行")