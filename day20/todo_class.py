class Todo:
    def __init__(self, content):
        self.content = content
        self.done = False

    def mark_done(self):
        self.done = True

    def show(self):
        if self.done:
            print(f"[✓] {self.content}")
        else:
            print(f"[ ] {self.content}")

    def to_dict(self):
        return {"content": self.content, "done":self.done}

import os
import json

class TodoManager:
    def __init__(self, filename):
        self.filename = filename
        self.todos = []
        self.load()

    def load(self):
        if not os.path.exists(self.filename):
            return
        #文件存在，继续读
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                todo = Todo(item["content"])
                todo.done = item["done"]
                self.todos.append(todo)

    def save(self):
        data = []
        for todo in self.todos:
            s1 = todo.to_dict()
            data.append(s1)
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2 )
    
    def add(self, content):
        todo = Todo(content)
        self.todos.append(todo)
        self.save()
        print("已添加")

    def show_all(self):
        if not self.todos:
            print("暂无待办")
            #break
            #break只能用在for或while循环里，这里在if里，没有循环包着。运行会报错
            return
        for i, todo in enumerate(self.todos, 1):
            print(f"{i}. ", end = "")
            todo.show()

    def mark_done(self,index):
        if index < 0 or index >= len(self.todos):
            print("索引有误")
            return
        self.todos[index].mark_done()
        self.save()
        print("已标记完成")

    def delete(self, index):
        if index < 0 or index >= len(self.todos):
            print("索引有误")
            return
        del self.todos[index]
        self.save()
        print("已删除")

def main():
    manager = TodoManager("todos.json")

    while True:
        print("\n1. 添加待办")
        print("2. 查看待办")
        print("3. 标记完成")
        print("4. 删除待办")
        print("5. 退出")

        choice = input("请选择：")

        if choice == "1":
            content = input("请输入待办内容：")
            manager.add(content)

        elif choice == "2":
            manager.show_all()

        elif choice == "3":
            index_str = input("请输入要完成的待办序号：")
            try:
                index = int(index_str)
                manager.mark_done(index - 1)
            except ValueError:
                print("请输入数字")

        elif choice == "4":
            index_str = input("请输入要删除的待办序号：")
            try:
                index = int(index_str)
                manager.delete(index - 1)
            except ValueError:
                print("请输入数字")

        elif choice == "5":
            print("再见")
            break

        else:
            print("输入有误")


main()     

t1 = Todo("学习Python")
t1.show()
print(t1.to_dict())

t2 = Todo("写代码")
t2.mark_done()
t2.show()
print(t2.to_dict())

manager = TodoManager("test_todos.json")
manager.todos.append(Todo("测试1"))
manager.todos.append(Todo("测试2"))
manager.todos[1].mark_done()
manager.save()