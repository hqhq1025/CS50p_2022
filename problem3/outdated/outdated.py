list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
date = input("PLease enter the date.")
date = date.replace("/"," ").replace(","," ")
month,day,year = date.split()
month = month.title()
for index,m in enumerate(list):
    if m == month:
            month = index + 1
if int(day) <= 31 and int(month) <= 12:
    print(f"{year:02}",end="")
    print(f"-{int(month):02}-{int(day):02}")
#还是不行