text = "    Hello,Python World  "

print(text.strip())#去首尾空格
print(text.lower())#转小写
print(text.upper())#转大写
print(text.replace("Python","AI"))#替换
print(text.split(","))#按逗号拆分  拆分成列表了
print("-".join(["a","b","c"]))#拼接
print(text.count("1"))#统计出现次数
print(text.find("Python"))#查找位置，找不到返回-1

print("123".isdigit())#是否全是数字
print("abc".isalpha())#是否全是字母
print("abc123".isalnum())#是否字母或数字