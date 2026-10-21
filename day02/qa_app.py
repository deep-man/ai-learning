#问答小程序
name = input("你叫什么名字？")
city = input("你来自哪个城市？")
age = int(input("你多大了？"))
hours = float(input("每天学几个小时？"))

next_age = age + 1
weekly_hours = hours * 7

print("\n=====你的信息=====")
print(f"你好，{name}!")
print(f"你来自{city}，今年{age}岁。")
print(f"明年你就{next_age}岁了。")
print(f"每天学{hours}小时，一周就是{weekly_hours}小时")
print("加油，坚持就是胜利")

goal = input("你学习AI的目标是什么？")
print(f"你的目标是：{goal},祝你早日实现")