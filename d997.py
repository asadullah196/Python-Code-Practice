#Practice basic functions today

userNum = int(input("Please write a number: "))


def convert_binary_num(num):
    if num > 1:
        convert_binary_num(num//2)
    print(num % 2, end='')


convert_binary_num(userNum)