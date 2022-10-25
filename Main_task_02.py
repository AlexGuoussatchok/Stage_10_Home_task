# Alex Goussatchok
# QA 4822
# Task: Fibonacci by index
# v 1.0

def user_input():
    index = int(input("Please enter a number for index search: "))
    return index


def find_fibonacci_number(index):
    num_1 = 0
    num_2 = 1
    i = 0
    while i < index - 2:
        num_sum = num_1 + num_2
        num_1 = num_2
        num_2 = num_sum
        i += 1

    return num_2


def user_output(msg):
    print(msg)

def main():
    index = user_input()
    num_2 = find_fibonacci_number(index)
    msg = f"{num_2} is a number with serial number {index} from Fibonacci sequence"
    print(msg)


main()