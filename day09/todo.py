todos = []

while True:
    print("\n1.添加待办")
    print("2.删除待办")
    print("3.查看待办")
    print("4.退出")
    choice = input("请选择：")

    if choice == "1":
        item = input("请输入待办内容：")
        todos.append(item)
        print("已添加")
    elif choice == "2":
        item = input("输入要删除的内容：")
        if item in todos:
            todos.remove(item)
            print("已删除")
        else:
            print("没有这条待办")
    elif choice == "3":
        if len(todos) == 0:
            print("暂无待办")
        else:
            for i,item in enumerate(todos,1):
                print(f"{i}.{item}")
    elif choice == "4":
        print("再见")
        break
    else:
        print("输入有误")
        
