coin = 50
print("Amount Due: 50")

while coin > 0:
    add = int(input("Insert Coin: "))
    # 检查插入的硬币是否为 25, 10 或 5
    if add in [25, 10, 5]:
        coin -= add  # 减去插入的硬币
        if coin > 0:
            print("Amount Due: " + str(coin))
        else:
            print("Change Owed: " + str(abs(coin)))
    else:
        print("Amount Due: " + str(coin))
