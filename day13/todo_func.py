def show_menu():
    print("\n1.添加待办")
    print("2.删除待办")
    print("3.查看待办")
    print("4.退出")

def add_todo(todos):
    item  = input("请输入你要添加的内容：")
    todos.append(item)
    print("已添加")

def delete_todo(todos):
    item = input("请输入你要删除的内容：")
    if item in todos:
        todos.remove(item)
        print("已删除")
    else:
        print("没有这条待办")

def show_todos(todos):
     if len(todos) == 0:
        print("暂无待办")
     else:
         for i,item in enumerate(todos,1):
            print(f"{i}.{item}") 

todos = []
def main():
    while True:
        show_menu()
        choice = input("请输入选择：")
        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            delete_todo(todos)
        elif choice == "3":
            show_todos(todos)
        elif choice == "4":
            break
        else:
            print("输入有误")

main()