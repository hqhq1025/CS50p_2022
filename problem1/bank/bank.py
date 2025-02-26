greet = input("Please greet.")
money = 100

# 去除标点符号，例如逗号
greet = greet.replace(',', '')

word = greet.lower().strip().split()

if word[0] == 'hello':
    money = 0
elif word[0].startswith('h'):
    money = 20

print("$"+str(money))