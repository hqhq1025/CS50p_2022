while True:
    try:
        per = input("Please enter.")
        son,mother = per.split("/")
        
        #print(per)
        son = int(son)
        mother = int(mother)
        if son > mother:
            raise ValueError
        per = round(100*eval(per))
        if per >= 99:
            print("F")
        elif per <= 1:
            print("E")
        else:
            print(str(per) + "%")
        break
    except (ValueError,ZeroDivisionError):
        print("Invalid input.")