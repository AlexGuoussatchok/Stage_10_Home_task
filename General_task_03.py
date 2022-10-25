# Alex Goussatchok
# QA 4822
# Task: All primes in sequence
# v 1.0


def user_input():
    index = int(input("Please enter the last number of sequence: "))
    return index


def create_sequence(number, index, sequence):
    while len(sequence) - 1 < index:
        for j in range(2, number):
            if number % j == 0:
                number += 1
                break

        else:
            sequence.append(number)
            number += 1


def main():
    index = user_input()
    sequence = []
    number = 2
    create_sequence(number, index, sequence)

    print(sequence)


main()
