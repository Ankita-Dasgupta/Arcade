import random


def value(n):
    if n == 'I':
        return 1
    elif n == 'V':
        return 5
    elif n == 'X':
        return 10
    elif n == 'L':
        return 50
    elif n == 'C':
        return 100
    elif n == 'D':
        return 500
    elif n == 'M':
        return 1000
    else:
        return 0
for var in range(10):
    roman= "none"

    player=random.randrange(1,100)
    print(player,"convert this number to roman")
    converted=input("converted number")
    while roman != "0":
     roman = converted
     if roman=="0":
         break

     res = 0
     i = 0

     while i < len(roman):
            s1 = value(roman[i])

            if i+1 < len(roman):
                s2 = value(roman[i+1])

                if s1 >= s2:
                    res = res+s1
                    i = i+1

                else:
                    res = res+(s2-s1)
                    i = i+2
            else:
                res = res+s1
                i = i+1

     if player==res:
         print("good job")
     else:
         print("wrong")

     break
