import csv
with open("scores1.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "语文", "数学", "英语"])
    writer.writerow(["小明", 85, 92, 78])
    writer.writerow(["小红", 90, 88, 95])
    writer.writerow(["小刚", 70, 75, 80])

def load_students(filename):
    #读CSV：按字典读（推荐）
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            nums = []
            for row in reader:
                nums.append(row)
            return nums
    except FileNotFoundError:
        print("文件不存在")
        return []

def calc_student_stats(students):
    results = []
    for student in students:
        chinese = int(student["语文"])
        math = int(student["数学"])
        english = int(student["英语"])
        total = chinese + math + english
        avg = total / 3
        results.append({"姓名":student["姓名"], "总分":total, "平均分":avg})
    return results

def calc_subject_avg(students):
    chinese_total = 0
    math_total = 0
    english_total = 0
    for student in  students:
        chinese_total += int(student["语文"])
        math_total += int(student["数学"])
        english_total += int(student["英语"])
    chinese_avg = chinese_total / len(students)
    math_avg = math_total / len(students)
    english_avg = english_total / len(students)
    return chinese_avg,math_avg,english_avg

def find_top_student(stats):
    top_name = stats[0]["姓名"]
    top_total = stats[0]["总分"]
    for student in stats:
        if student["总分"] > top_total:
            top_total = student["总分"]
            top_name = student["姓名"]
    return top_name, top_total

def main():
    student_scores = load_students("scores1.csv")
    results = calc_student_stats(student_scores)
    chinese_avg,math_avg,english_avg = calc_subject_avg(student_scores)
    # print(f"语文平均分：{chinese_avg:.2f}")
    # print(f"数学平均分：{math_avg:.2f}")
    # print(f"英语平均分：{english_avg:.2f}")
    for r in results:
        print(f"{r['姓名']}：总分{r['总分']}，平均分{r['平均分']:.2f}")
    top_name,top_total = find_top_student(results)
    print(f"总分最高的学生名称是：{top_name}，分数为{top_total}")
main()
# with open("student.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)
#     for row in reader:
#         print(row["姓名"], row["数学"])