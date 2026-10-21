username = input("请输入用户名：")
password = int(input("请输入密码："))

if username == "admin" and password == 123456:
    print("登录成功")
elif username == "admin" and password != 123456:
    print("密码错误")
elif username != "admin" and password == 123456:
    print("用户名不存在")
else:
    print("密码和用户名都错误")


username = input("请输入用户名：")
password = input("请输入密码：")

if username == "admin" and password == "123456":
    print("登录成功")
elif username == "admin":
    print("密码错误")
else:
    print("用户名不存在")