# def get_level(score):
#     if score > 100 or score < 0:
#         print("输入有误")
#     elif score == 100:
#         print("满分")
#     elif score >= 90:
#         print("优秀")
#     elif score >= 80:
#         print("良好")
#     elif score >= 60:
#         print("及格")
#     else:
#         print("不及格")

# get_level(90)

def get_level(score):
    if score > 100 or score < 0:
        return("输入有误")
    elif score == 100:
        return("满分")
    elif score >= 90:
        return("优秀")
    elif score >= 80:
        return("良好")
    elif score >= 60:
        return("及格")
    else:
        return("不及格")

score = int(input("请输入分数："))
level = get_level(score)
print(f"你的等级是：{level}")
# #return后面多了括号
# return是关键字，不是函数，不需要括号
# return "优秀"