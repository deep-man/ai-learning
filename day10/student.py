student = {"name":"程宏建","age":32,"city":"武汉","分数":98}

# while True:
#     print("\n1、查看信息")
#     print("2、修改分数")
#     print("3、退出")
#     choice  = input("请输入你选择的内容：")

#     if choice == "1":
#         for key,value in student.items():
#             print(key,value)
#     elif choice == "2":
#         print("请输入需要修改的分数")
#         student["分数"] = int(input())
#         for key,value in student.items():
#                     print(key,value)
#     else:
#         print("再见")
#         break

while True:
     print("\n1、查看信息")
     print("2、修改分数")
     print("3、退出")
     choice  = input("请输入你选择的内容：")

     if choice == "1":
          for key,value in student.items():
               print(key,value)
     elif choice == "2":
          new_score = int(input("请输入新的分数："))
          student["分数"] = new_score
          print("修改成功")
     elif choice == "3":
          print("再见")
          break
     else:
          print("输入有误，请重新选择")