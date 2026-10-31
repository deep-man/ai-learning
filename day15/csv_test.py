#CSV是逗号分隔的文本文件，用Excel能直接打开

import csv

#写CSV
with open("student.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "语文", "数学", "英语"])
    writer.writerow(["小明", 85, 92, 78])
    writer.writerow(["小红", 90, 88, 95])

# newline="" 防止 Windows 下多空行
# writerow() 写一行
# writerows() 写多行

#读CSV：按行读
with open("student.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
#读出来都是字符串，数字要自己转

#读CSV：按字典读（推荐）
with open("student.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
    for row in reader:
        print(row["姓名"], row["数学"])
#DictReader用表头做键，取数据更方便

#CSV：按字典写
data = [
    {"姓名":"小明", "数学":92},
    {"姓名":"小红", "数学":88},
]

with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["姓名", "数学"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

#DictWriter必须传fieldnames
#先writeheader()，再写数据
#字典的键要和fieldnames对得上
#写文件用newline=""，中文用encoding="utf-8"
# csv.DictWriter 就是：你给字典，它按 fieldnames 的顺序写成 CSV 行。
# 表头用 writeheader() 自动写，数据用 writerow() 或 writerows() 写。