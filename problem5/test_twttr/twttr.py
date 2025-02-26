# twttr.py

def main():
    # 获取用户输入并调用shorten函数
    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(word):
    # 元音字母列表，包含大写和小写
    vowels = "AEIOUaeiou"
    # 使用列表推导式过滤掉元音
    return ''.join([char for char in word if char not in vowels])

if __name__ == "__main__":
    main()