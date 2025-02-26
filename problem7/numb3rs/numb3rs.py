import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    flag = re.match(r"^0-255\.0-255\.0-255\.0-255",ip)
    if flag:
        return True
    else:
        return False



if __name__ == "__main__":
    main()