import re

print("AWESOME CALCULATOR")

previous = 0
run = True

def performMath(choice, number):
    print("p", previous)
    if choice==1:
        return previous+number
    elif choice==2:
        return previous-number
    elif choice==3:
        return previous*number
    elif choice==4:
        return previous/number




while run:

    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Done")
    op = int(input("Choice: "))
    if op==5:
        run == False
        break
    number = int(input("Number: "))
    answer = performMath(op,number)
    print("Answer:", answer)
    previous = answer
