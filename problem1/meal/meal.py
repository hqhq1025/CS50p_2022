def main():
    time = input("Please enter the time.")
    timed = convert(time)
    match timed:
        case _ if 7 <= timed <= 8:
            print("breakfast time")
        case _ if 12 <= timed <= 13:
            print("lunch time")
        case _ if 18 <= timed <= 19:
            print("dinner time")

def convert(time):
    sp = time.split(":")
    timed = float(sp[0]) + float(sp[1])/60
    return timed


if __name__ == "__main__":
    main()