num = input("Please enter.")
num = num.lower().strip()
match num:
    case '42' | 'forty-two' | 'forty two':
        print("Yes")
    case _:
        print("No")
