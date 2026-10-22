fruits = ["apple","banana","orange"]

for fruit in fruits:
    print(fruit)

#enumrate是Python内置函数，作用是遍历列表时，同时给出“索引”和“元素”
# enumerate(列表) 遍历时同时给索引和元素；
# for i, x in enumerate(列表) 把索引给 i，元素给 x；
# 第二个参数可以指定索引起始值。
for i,fruit in enumerate(fruits):
    print(i,fruit)