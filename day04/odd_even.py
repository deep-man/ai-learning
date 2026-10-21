name = int(input("请输入一个数字："))
if name == 0:
    print("你输入的数字为0")
elif name % 2 == 1 or name % 2 == -1:
    print("你输入的数字为奇数")
else:
    print("你输入的数字为偶数")

#需要说明一点-3 % 2 的结果为1不是-1
#所以更加简洁的方法是name % 2 != 0
#原因是Python的%结果，符号跟除数一致