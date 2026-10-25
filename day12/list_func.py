# def analyze(nums):
#     return sum(nums),max(nums),min(nums),len(nums)

# nums = [3, 4, 5, 6, 7]
# total,high,lower,weight = analyze(nums)
# print(total, high, lower, weight)

# def analyze(nums):
#     return sum(nums), max(nums), min(nums), sum(nums) / len(nums)

# nums = [3, 4, 5, 6, 7]
# total, max_num, min_num, avg = analyze(nums)
# print(f"总和：{total}")
# print(f"最大值：{max_num}")
# print(f"最小值：{min_num}")
# print(f"平均值：{avg}")

#输入列表的三种常见方式
# 方式1：代码里直接写死（最简单）
# nums = [3, 4, 5, 6, 7]
#方式二：输入一串数字，用空格分隔
text = input("请输入数字，用空格分隔:")
nums = text.split()
nums = [int(x) for x in nums]
print(nums)
#方式三：输入逗号分隔
text = input("请输入数字，用空格分隔:")
nums = text.split(",")
nums = [int(x) for x in text.split(",")]
print(nums)