import math


def isValid(num):
    valid = True
    if(len(num) > 9):
        valid = False
    for digit in num:
        #print(digit)
        #print(digit != 1 and digit != 0)
        if digit != "1" and digit != "0":
            
            valid = False
            break

    
    return valid


def convert(num):
    aux = reversed(num)
    sum = 0
    i = 0
    for digit in aux:
        sum += int(digit) * (math.pow(2, i))
        i+=1
    
    print("The binary is converted!")
    print("Result: " + str(sum))


number = input("Input a binary number up to 8 digits:")
#print(len(number))
if isValid(number):
    convert(number)
else:
    print("Invalid input!")
