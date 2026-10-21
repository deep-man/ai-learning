#成绩等级判断
name = input("请输入你的名字：")
score = float(input("请输入你的分数（0-100）："))

if score == 100:
    print("满分！太厉害了！")
    
if score < 0 or score > 100:
    print("分数输入有误，请输入0-100之间的数")
elif score >= 90:
    print(f"{name},你的等级是：优秀")
elif score >= 80:
    print(f"{name},你的等级是：良好")   
elif score >= 70:
    print(f"{name},你的等级是：中等")
elif score >= 60:
    print(f"{name},你的等级是：及格")
else:
    print(f"{name},你的等级是：不及格，要加油！")