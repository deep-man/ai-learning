import json

def load_students(filename):
      try:
        with open(filename, "r", encoding="utf-8") as f:
            students = json.load(f)
            return students
      except FileNotFoundError:
        return []

def save_students(students,filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)

def add_student(students):
    name = input("请输入学生姓名：")
    #遍历是否重名
    for s in students:
        if s["姓名"] == name:
            print("学生已存在")
            return students
    try:
        chinese = int(input("语文："))
        math = int(input("数学："))
        english = int(input("英语："))
    except ValueError:
        print("输入值类型错误,请重新添加")
        return students

    student = {"姓名": name, "语文": chinese, "数学": math, "英语": english}

    students.append(student)
    print("添加成功")
    return students

def show_students(students):
    results = []
    if len(students) == 0:
        print("暂无学生")
        return []
    else:
        for student in students:
            chinese = int(student["语文"])
            math = int(student["数学"])
            english = int(student["英语"])
            total = chinese + math + english
            avg = total / 3
            print(f"{student['姓名']}：语文{chinese}，数学{math}，英语{english}，总分{total}，平均分{avg:.2f}")
        

def main():
    students = load_students("students.json")
    filename = "students.json"
    while True:
        print("1、添加学生:\n")
        print("2、查看学生:\n")
        print("3、保存并退出:\n")
        choice = input("请选择输入项：")
        if choice == "1":
            students = add_student(students)
            save_students(students,filename)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            save_students(students,filename)
            print("已保存，退出")
            break
        else:
            print("输入有误，请重新选择")
main()        