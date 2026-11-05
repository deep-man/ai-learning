import csv

with open("sales.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["日期", "产品", "单价", "数量"])
    writer.writerow(["2026-01-01", 'A', 10, 5])
    writer.writerow(["2026-01-02", 'B', 20, 3])
    writer.writerow(["2026-01-03", 'A', 10, 8])
    writer.writerow(["2026-01-04", 'C', 15, 2])
    writer.writerow(["2026-01-05", 'B', 20, 6])

import pandas as pd

sales = pd.read_csv("sales.csv", encoding="utf-8")
print(sales)
sales["销售额"] = sales["单价"] * sales["数量"]
print(sales)
print(sales.sort_values("销售额",ascending=False).head(1))
print(sales[sales["产品"] == 'A'])
print(sales[sales["销售额"] > 100])
sales = sales.sort_values("销售额")
print(sales)
sales.to_csv("sales_result.csv", index=False, encoding="utf-8")