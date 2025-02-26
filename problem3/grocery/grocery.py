goods = {}
while True:
    try:
        item = input().lower()
        if item in goods:
            goods[item] += 1
        else:
            goods[item] = 1
        
        
    except EOFError:
        print()
        for item in sorted(goods):
            print(str(goods[item])+" "+item.upper())
        break