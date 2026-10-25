nums = [3, 7, 2, 9, 5]

print(len(nums)) #长度
print(sum(nums)) #求和
print(max(nums)) #最大值
print(min(nums)) #最小值
print(sorted(nums)) #排序，返回列表
print(sorted(nums,reverse = True)) #排序

nums.sort() #原地排序
print(nums)


nums.reverse() #原地反转
print(nums)

#注意：sorted() 不改原列表，sort() 改原列表。