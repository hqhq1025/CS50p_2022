import csv
import sys
from tabulate import tabulate

# 检查命令行参数
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

students = []

try:
    # 打开并读取 CSV 文件
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        
        # 获取 CSV 的表头（列名）
        headers = reader.fieldnames
        
        for row in reader:
            students.append(row)

    # 使用 tabulate 打印表格
    print(tabulate(students, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")