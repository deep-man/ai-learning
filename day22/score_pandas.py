import pandas as pd
score = pd.read_csv("students.csv", encoding="utf-8")
print(score.head(3))
print(score.shape)
score["平均分"] = (score["语文"] + score["数学"] + score["英语"]) /3
print(score["平均分"])
# print(score["语文"].mean())
# print(score["数学"].mean())
# print(score["英语"].mean())
print(score[["语文", "数学", "英语"]].mean())
score["总分"] =  score["语文"] + score["数学"] + score["英语"]
score = score.sort_values("总分", ascending=False)
print(score)
#排序后没保存排序结果
#sort_values默认不修改原数据，只是返回排序后的副本
print(score[score["数学"] >= 90][["姓名","数学"]])
score.to_csv("students_result.csv", index=False, encoding="utf-8")