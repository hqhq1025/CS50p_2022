import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a Python file")
counts = 0

raw = []
buffer = []

try:
    with open(sys.argv[1],"r") as file1:
        reader = csv.DictReader(file1)
        headers = reader.fieldnames
        new_headers = ["first", "last", "house"]
        with open(sys.argv[2],"w") as file2:
            writer = csv.DictWriter(file2,fieldnames=new_headers)
            writer.writeheader()
            for row in reader:
                first = row["name"].split()[1]
                last = row["name"].split()[0].strip(",")
                writer.writerow({"first":first, "last":last, "house": row["house"]})
        
            
except FileNotFoundError:
    sys.exit("File does not exist")