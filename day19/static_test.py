class MathTool:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0


print(MathTool.add(3, 5))
print(MathTool.is_even(4))

#静态方法的特点
# 用@staticmethod装饰
# 没有self参数
# 不访问实例属性，也不访问类属性
# 只是“放在类里的普通函数”

# 什么时候用：
# 工具函数，和类相关但不需要对象数据
# 比如“判断偶数”“格式化日期”