#第一题
#age = input("年龄：")
#第一种方法age = int(input("年龄："))
#第二种方法age = int(age)
#next_age = age + 1
#print(f"明年你{next_age}岁")

#第二题
#第三题
#第四题
grade = int(input("请输入分数（0-100）："))
if grade > 100 or grade < 0:
    print("你的输入有误")
elif grade == 100:
    print("你的成绩是满分")
elif grade >= 90:
    print(f"你的成绩是{grade}，等级是优秀")
elif grade >= 80:
    print(f"你的成绩是{grade}，等级是良好")
elif grade >= 60:
    print(f"你的成绩是{grade}，等级是及格")
else:
    print(f"你的成绩是{grade}，等级是不及格")

