#类变量
class Student:
    school = "第一中学"
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    def show(self):
        print(f"{self.name},{self.school}")

s1 = Student("小明")
s2 = Student("小红")

s1.show()
s2.show()
print(f"学生总数:{Student.count}")

# 类变量 vs 实例变量
# 类型	         定义位置	                访问方式	           归属
# 类变量	  类里面，方法外面	    类名.变量 或 self.变量	所有对象共享
# 实例变量	__init__ 里 self.xxx	  self.xxx	          每个对象独立

#类变量：所有对象共享的数据，如学校名、总人数
#实例变量：每个对象独有的数据，如姓名、年龄