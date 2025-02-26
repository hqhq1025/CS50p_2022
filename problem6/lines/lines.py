import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
counts = 0

try:
    with open(sys.argv[1],"r") as file:
        lines = file.readlines()
        for line in lines:
            if line.strip().startswith("#") or (not line.strip()):
                continue
            else:
                counts += 1
                
except FileNotFoundError:
    sys.exit("File does not exist")

print(counts)