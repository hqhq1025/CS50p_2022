import inflect

# 创建 inflect 引擎
p = inflect.engine()

# 存储输入的名字
names = []

# 提示用户输入名字
print("Enter names (press Ctrl+D to finish):")

while True:
    try:
        name = input("Name: ")
        names.append(name)
    
    except EOFError:
        # 整理句子
        if names:
            sentence = f"Adieu, adieu, to {p.join(names)}"
            print(sentence)
        break