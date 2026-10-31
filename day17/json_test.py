import json

#1.json.dumps():Python对象——JSON字符串
student = {"name":"小明", "age":20, "city":"北京"}
text = json.dumps(student, ensure_ascii=False)
print(text)
#ensure_ascii=False让中文正常显示，不然会变成\uXXX
#返回的是字符串，不是文件

#2.json.loads():JSON字符串——Python对象
#参数：一个字符串，内容必须是合法的JSON格式
#返回：Python的字典、列表、字符串、数字、布尔值或None
import json

text = '{"name": "小明", "age":20}'
student = json.loads(text)
print(student)
print(student["name"])

#3.json.dump():Python对象——写入文件
import json

student = {"name": "小明", "age":20, "city":"北京"}

with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student, f, ensure_ascii=False, indent=2)

#indent=2让文件格式化，方便阅读
#ensure_ascii=False让中文正常写入
#写文件用"w"

#4.json.load():从文件读取——Python对象
import json

with open("student.json", "r", encoding="utf-8") as f:
    student = json.load(f)

print(student)
print(student["name"])

#读文件用"r"
#返回的是字典或列表

data = {
    "name":"小明",
    "age":20,
    "is_student":True,
    "score":None,
    "hobbies":["读书", "跑步"],
    "address":{"city":"北京", "district":"朝阳"}
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False,indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["hobbies"])
print(data["address"]["city"])

#JSON可以嵌套字典和列表，这点和Python一样
# 错误	                                            原因
# json.decoder.JSONDecodeError	     JSON 格式不对，比如单引号、末尾多逗号
# 中文变成 \uXXXX	                      没加 ensure_ascii=False
# FileNotFoundError	                   文件不存在，读之前要判断
# 写入后中文乱码	                          没加 encoding="utf-8"