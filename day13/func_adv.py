def greet(name, greeting = "你好"):
    return f"{greeting},{name}"

print(greet("小明"))
print(greet("小明","早上好"))
#目的是：常用值设成默认，调用时不用每次重复写；需要时还能临时改
# 实际用途
# 后面写代码会经常遇到：
# 场景	         默认参数的作用
# 连接数据库	 host="localhost"，本地不用传
# 读文件	     encoding="utf-8"，默认编码
# 发请求	     timeout=10，默认超时
# 日志	         level="INFO"，默认级别
# 文本清洗	     lower=True，默认转小写
# 一句话：默认参数让函数“开箱即用”，又保留灵活性。

#练习1的目的
#1、哪些参数适合设默认值：大多数调用都一样的值
#2、默认参数放最后：因为位置参数要按顺序传
#3、调用时可以省略：不传就用默认，传了就覆盖

def get_min_max(nums):
    return min(nums), max(nums)

low, high = get_min_max([3, 7, 3, 9, 5])
print(f"最小值：{low}")
print(f"最大值：{high}")
#一次调用，拿到三个结果
#直接赋值给三个变量，名字清楚
#本质是返回一个元组（总和、最大值、最小值）

def get_level(score):
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    return "不及格"

def report(name,score):
    level = get_level(score)
    return f"{name}的成绩是{score},等级是{level}"

print(report("程宏建",85))