# Alex Goussatchok
# QA 4822
# Task: Perfect number
# v 1.0


def user_input():
    num = int(input("Please enter a number for a check: "))
    return num


def calculate_dividers(num):
    dividers_summ = 0
    for i in range(1, num-1):
        if num % i == 0:
            dividers_summ += i
    return dividers_summ


def compare(num, dividers_summ):
    if num != dividers_summ:
        return False
    else:
        return True


def user_output(msg):
    print(msg)


def main():
    num = user_input()
    dividers_summ = calculate_dividers(num)
    if compare(num, dividers_summ) == True:
        msg = f"The number {num} is a perfect number"
    else:
        msg = f"The number {num} is not a perfect number"
    user_output(msg)


main()
