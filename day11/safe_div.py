try:
#   a, b = int(input("请输入两个数字："))
#   int(input(...))只得到一个整数，不能拆给a和b两个变量
    a = int(input("请输入被除数："))
    b = int(input("请输入除数："))
    if  b  == 0:
        print("除数不能为0")
    else:
        c = a / b
        print(f"输出结果：{c}")
except ValueError:
    print("请输入数字")
finally:
    print("计算结束")


try:
#   a, b = int(input("请输入两个数字："))
#   int(input(...))只得到一个整数，不能拆给a和b两个变量
    a = int(input("请输入被除数："))
    b = int(input("请输入除数："))
    c = a / b
    print(f"输出结果：{c}")
except ValueError:
    print("请输入数字")
except ZeroDivisionError:
    print("除数不能为0")
finally:
    print("计算结束")