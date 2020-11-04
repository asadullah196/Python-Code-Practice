#Basic python function practice day
basicNum = input("Please put the besic number: ")
squireNum = int(input("Please write a number for squire it: "))
swapOne = input("Your swap number One: ")
swapTwo = input("your swap number two: ")
evenOddNum = int(input("Write a number for Event Odd testing: "))


def basic_function(x):
    print(f"You Passed {x}")


def squire_function(t):
    temp = t**2
    print(f"Your number is {t} and Squire is {temp}")


def swap_number(x, y):
    temp = x
    x = y
    y = temp
    print(f"Your two number is {x} and {y}, The swap number is {x} , {y}")


def check_even_odd(x):
    temp = x % 2
    if temp == 0:
        print(f"Your number is {x} and It's Even")
    else:
        print(f"Your number is {x} and It's Odd")


basic_function(basicNum)
squire_function(squireNum)
swap_number(swapOne, swapTwo)
check_even_odd(evenOddNum)












