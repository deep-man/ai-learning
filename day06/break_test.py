count = 0

while True:
    print("循环中")
    count += 1
    if count == 3:
        break

total = 0
num = 1

while num <= 5:
    total += num
    num += 1

print(f"1到5的和是{total}")