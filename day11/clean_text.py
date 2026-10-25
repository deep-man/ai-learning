# 题目1：文本清洗工具
# 新建 clean_text.py。
# 要求：
# 输入一段文字
# 去掉首尾空格
# 转小写
# 把中文逗号 ， 替换成英文逗号 ,
# 统计文字长度
# 输出清洗后的文字和长度

text = str(input("请输入一段文字："))
#input()返回的已经是字符串，外面再包str()没意义
text_strip = text.strip()
text_lower = text_strip.lower()
text_replace = text_lower.replace("，",",")
text_len = len(text_replace)
#变量太多，可以链式调用
text = input("请输入一段文字：").strip().lower().replace("，",",")

text = input("请输入一段文字")
cleaned = text.strip().lower().replace("，",",")

print(f"清洗之后的文字：{text_replace}")
print(f"清洗之后的文字的长度：{text_len}")



