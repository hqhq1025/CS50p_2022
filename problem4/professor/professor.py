import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    correct = 0  # 初始化正确答案计数
    up_lim = pow(10, level)
    lo_lim = pow(10, level - 1)
    
    if level == 1:
        lo_lim = 0

    for _ in range(10):
        false_attempts = 0
        a = random.randint(lo_lim, up_lim - 1)
        b = random.randint(lo_lim, up_lim - 1)
        ans = a + b

        while True:
            try:
                userans = int(input(f"{a} + {b} = "))
                if userans == ans:
                    correct += 1
                    break
                else:
                    print("EEE")
                    false_attempts += 1
                    if false_attempts == 3:
                        print(f"{a} + {b} = {ans}")
                        break
            except ValueError:
                print("EEE")
                false_attempts += 1
                if false_attempts == 3:
                    print(f"{a} + {b} = {ans}")
                    break

    print(f"Score: {correct}")  # 输出正确答案的计数

if __name__ == "__main__":
    main()