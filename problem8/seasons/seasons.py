from datetime import date
import inflect
import sys

inf = inflect.engine()

def main():
    birthday = input("Date of Birth:")
    try:
        birthday = date.fromisoformat(birthday)
    except ValueError:
        sys.exit("Invalid date.")
    today = date.today()
    interval = count_days(birthday ,today)
    min = inf.plural('minute',interval)
    print(inf.number_to_words(interval,andword="").capitalize() + " "+ min)

def count_days(birthday,today):
    interval = today - birthday
    interval = interval.days*24*60
    return interval


if __name__ == "__main__":
    main()
