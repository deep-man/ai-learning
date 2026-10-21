age = int(input("你多大了？"))

if age >= 18:
    print("你成长了")
else:
    print("你还没成年")

score = int(input("请输入分数"))

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")