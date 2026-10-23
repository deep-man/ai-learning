student = {"name":"小明","age":20,"city":"北京"}

print(student)
print(student["name"])
print(student["age"])

student = {"name":"小明","age":20}
print(len(student))
print("name" in student)
print("score" in student)

student = {"name":"小明","age":20}

student["city"] = "北京"
print(student)

del student["city"]
print(student)

age = student.pop("age")
#pop(键) = 删除这个键，并把它对应的值返回给你。
print(age)
print(student)

stduent = {"name":"小明"}
print(student.get("name"))
print(student.get("score"))
print(student.get("score",0))