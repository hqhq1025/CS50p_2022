tw = input("Please enter.")
for i in tw:
    if i.lower() in ['a','e','i','o','u']:
        continue
    else:
        print(i,end="")
print()