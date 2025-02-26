def main():
    greet = input("Please greet.")
    print("$"+str(value(greet)))

def value(greeting):
    money = 100
    greeting = greeting.replace(',', '')
    word = greeting.lower().strip().split()
    if word[0] == 'hello':
        money = 0
    elif word[0].startswith('h'):
        money = 20
    return money

if __name__ == "__main__":
    main()