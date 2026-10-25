def clean_text(text):
    text_strip = text.strip()
    text_lower = text_strip.lower()
    text_replace = text_lower.replace("，",",")
    return text_replace

text = input("请输入一段文字：")
print(f"清洗之后的文字：{clean_text(text)}")
