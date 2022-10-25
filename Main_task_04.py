# Alex Goussatchok
# QA 4822
# Task: Elements of Fibonacci sequence
# v 1.0

def user_input():
    index = int(input("Please enter a number for index search: "))
    return index


def create_fibonacci_sequence(index, fibonacci_sequence):
    num_1 = 0
    num_2 = 1
    for _ in range(1, index - 1):
        num_sum = num_1 + num_2
        num_1 = num_2
        num_2 = num_sum
        if num_2 < index:
            fibonacci_sequence.append(num_2)


def user_output(msg):
    print(msg)


def main():
    index = user_input()
    fibonacci_sequence = [0, 1]
    create_fibonacci_sequence(index, fibonacci_sequence)
    msg = f"The Fibonacci sequence limited with index {index} is {fibonacci_sequence}"
    user_output(msg)


main()