camel = input("Please enter.")
for i in camel:
    if i.isupper():
        print("_", end = "")
        print(i.lower(),end="")
    else:
        print(i,end="")

print()
