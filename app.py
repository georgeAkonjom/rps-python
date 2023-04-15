intfirst = int(input("an integer"))
intsecond = 45
intthird = 2

if intfirst > intsecond and intfirst > intthird:
    biggest = intfirst
    print(biggest)
    if intsecond > intthird:
        bigger = intsecond
        big = intthird 
        print(bigger, big)
    else :
        bigger = intthird
        big = intsecond
        print(bigger, big)
elif intsecond > intfirst and intsecond > intthird:
    biggest = intsecond
    print(biggest)
    if intfirst > intthird:
        bigger = intfirst
        big = intthird
        print(bigger, big)
    else :
        bigger = intthird
        big = intfirst
        print(bigger, big)
elif intthird > intfirst and intthird > intsecond:
    biggest = intthird
    print(biggest)
    if intfirst > intsecond:
        bigger = intfirst
        big = intsecond
        print(bigger, big)
    else :
        bigger = intsecond
        big = intfirst
        print(bigger, big)

