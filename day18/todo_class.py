class Todo:
    def __init__(self, content):#新创建的待办，默认都是未完成的
        self.content = content
        self.done = False

    def mark_done(self):
        self.done = True

    def show(self):
        if self.done:
            print(f"[✓]{self.content}")
        else:
            print(f"[ ]{self.content}")

class TodoManager:
    def __init__(self):
        self.todos = []

    def add(self, content):
        self.todos.append(Todo(content))

    def show_all(self):
        if len(self.todos) != 0:
            for item in self.todos:
                item.show()
        else:
            print("暂无待办")

    def done(self, index):
        if index >=0 and index < len(self.todos):
            self.todos[index].mark_done()
            print(f"第{index}个待办标记完成")
        else:
            print("索引有误")

manager = TodoManager()
manager.add("学习Python")
manager.add("写代码")
manager.add("运动")

manager.show_all()
manager.done(0)
manager.show_all()
