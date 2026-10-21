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