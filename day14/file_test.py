# import os
# print(os.getcwd())
# #运行后输出的路径
# #写文件
# with open("test.txt", "w", encoding="utf-8") as f:
#     f.write("第一行\n")
#     f.write("第二行\n")

# "w" 是写入模式
# 文件不存在会创建
# 文件存在会清空重写
# encoding="utf-8" 支持中文
# with 会自动关闭文件

#想固定创建在脚本旁边
import os 

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "test.txt")

#写文件
with open(file_path, "w", encoding="utf-8") as f:
    f.write("      第一行\n")
    f.write("你好        \n")

#读文件
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

#按行读取
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

with open(file_path, "a", encoding="utf-8") as f:
    f.write("第三行\n")


# 模式	作用	文件不存在	文件存在
# "r"	     读	       报错	    正常读
# "w"	     写	       创建	   清空重写
# "a"	    追加	   创建	   末尾追加

import os

if os.path.exists("test.txt"):
    print("文件存在")
else:
    print("文件不存在")