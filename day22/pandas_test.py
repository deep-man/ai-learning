import csv

with open("students.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "语文", "数学", "英语"])
    writer.writerow(["小明", 85, 92, 78])
    writer.writerow(["小红", 90, 88, 95])
    writer.writerow(["小刚", 70, 75, 80])
    writer.writerow(["小美", 88, 95, 92])

import pandas as pd

df = pd.read_csv("students.csv", encoding="utf-8")
print(df)

# df_excel = pd.read_excel("students.xlsx")
# print(df_excel)

#sheet_name:读哪个工作表
# df = pd.read_excel("students.xlsx", sheet_name = "Sheet1")
# df = pd.read_excel("students.xlsx", sheet_name = 0)
#不写sheet_name，默认读第一个sheet

#读所有sheet
# all_sheets = pd.read_excel("students.xlsx", sheet_name=None)
#sheet_name=None返回一个字典
# print(all_sheets)

#遍历：
# for name, df in all_sheets.items():#获取键值对
#     print(f"工作表：{name}")
#     print(df)

# print(df.head())#前5行
# print(df.head(3))#前3行
# print(df.tail)#后5行
# print(df.shape)#(行数，列数)
# print(df.columns)#列名
# print(df.info())#数据类型和缺失情况
# print(df.describe())#数值列统计

#选列
# print(df["姓名"])
# print(df[["姓名","数学"]])
#一列用单方括号，多列用双方括号
#选行
# print(df.iloc[0])#第一行，按位置
# print(df.iloc[0:2])#前两行
#iloc按位置取，从0开始

#筛选行
# print(df[df["数学"] >= 90])
# print(df[(df["语文"] >= 80) & (df["数学"] >= 90)])
# print(df["姓名"] == "小明")
#多条件用&或|，不能用and/or,每个条件要加括号

#新增列
df["总分"] = df["语文"] + df["数学"] + df["英语"]
df["平均分"] = df["总分"] / 3
print(df)
#整列运算不用循环，直接加减乘除
print(df.sort_values("总分", ascending=False))#降序
df.sort_values("总分")#默认升序

df.to_csv("result.csv", index=False, encoding="utf-8")
#index = False表示不保存行索引，不加会多一列0,1,2,3