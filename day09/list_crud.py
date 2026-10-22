#增
fruits = ["apple","banana"]
fruits.append("orange")
print(fruits)
#append只能加到末尾

#插入
fruits.insert(1,"pear")
print(fruits)
#insert可以插入到任意位置

#删
fruits.remove("banana")
print(fruits)

#删除最后一个
fruits.pop()
print(fruits)

#改
fruits[0] = "grape"
print(fruits)

#查
print(fruits[0])
print("apple" in fruits)
