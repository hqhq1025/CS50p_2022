dict = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
money = 0
while True:
    try:
        item = input("Item:")
        dish = item.title()
        if dish in dict:
            money += dict[dish]
            print(f"${money:.2f}")
    except EOFError:
        print()
        break