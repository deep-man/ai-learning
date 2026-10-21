#要求：
#程序随机生成 1-100 的整数
#让用户输入猜测
#猜大了提示“太大了”
#猜小了提示“太小了”
#猜对了提示“恭喜你，猜对了！”

#import的意思是：导入（引入）一个模块
#导入整个模块 import random
#导入模块并起别名 import random as rd
#只导入模块里的某个功能 from random import randint
import random

number = random.randint(1,100)
guess_number = int(input("请输入你猜测的数字："))

if guess_number < 1 or guess_number > 100:
    print("你猜测的数字不符合要求，请输入1-100的数字")
elif guess_number == number:
    print("恭喜你猜对了！")
elif guess_number > number:
    print("太大了")
else:
    print("太小了")