# Alex Goussatchok
# QA 4822
# Task: simple divisors
# v 1.0


def user_input():
    number = int(input("Please enter a number: "))
    return number


def find_dividers(number, dividers_sequence):
    for i in range(2, number + 1):  # --> we don't need 1 in our result as we'll check the divider if it is a prime
        for j in range(1, number + 1):
            if i * j == number:
                dividers_sequence.append(i)


def find_prime_divider(dividers_sequence, prime_divider):
    for i in dividers_sequence:
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            prime_divider.append(i)

def user_output(msg):
    print(msg)


def main():
    number = user_input()
    dividers_sequence = []

    find_dividers(number, dividers_sequence)
    prime_divider = []
    find_prime_divider(dividers_sequence, prime_divider)
    msg = f"The list of dividers for the number {number} is: {dividers_sequence}. " \
          f"The list of primes among them is {prime_divider}"
    user_output(msg)


main()
