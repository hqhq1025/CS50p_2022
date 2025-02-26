def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif not(s[0].isalpha() and s[1].isalpha()):
        return False
 # 检查车牌中的字符是否合法
    found_digit = False
    for index, i in enumerate(s):
        if not (i.isalpha() or i.isdigit()):
            return False

        # 如果遇到第一个数字，开始检查后续部分
        if i.isdigit():
            if i == '0' and not found_digit:
                # 数字不能以 0 开头
                return False
            found_digit = True
            if not check_middle(s, index):
                return False
    return True
        #todo:完成检查数字是否出现在中间
        #目前思路：找到数字后挨个往后遍历，看有没有字母，有的话则是中间位置，返回false

def check_middle(s, index):
    # 检查从第一个数字之后，确保没有字母
    for i in range(index + 1, len(s)):
        if s[i].isalpha():
            return False
    return True


main()