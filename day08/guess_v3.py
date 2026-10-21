import random

number = random.randint(1,100)
count  = 0
max_times = 5

for count in range(1,6):
    guess_number = int(input("请输入猜测的数字（1-100）："))

    if guess_number < 1 or guess_number > 100:
        print("输入有误，请输入1-100")
        continue

    count += 1

    if guess_number == number:
        print(f"恭喜你，第{count}次猜对了！")
        break
    elif guess_number > number:
        print("太大了")
    else:
        print("太小了")
else:
    print(f"机会用完了，正确答案是{number}")