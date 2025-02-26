import random
while True:
    n = input("Level:")
    if n.isnumeric():
        if int(n) >= 1:
            break

num = random.randint(1, int(n))
while True:
    guess = input("Guess:")
    if not guess.isnumeric():
        print("Invalid input, please enter a number.")
        continue
    guess = int(guess)
    if guess > num:
        print("Too large!")
    elif guess < num:
        print("Too small!")
    else:
        print("Just right!")
        break