# Alex Goussatchok
# QA 4822
# Task: Prime number check
# v 1.0

def user_input():
    number = int(input("Please enter a number (more than 1) for a check: "))
    return number

def check_if_prime_number(number):
    result = "prime"
    if isinstance(number, bool) or not isinstance(number, int) or not (number >= 1):
        return -1
    else:
        for i in range(2, number - 1):
            if number % i == 0:
                result = "not a prime"
        return result



def main():
    number = user_input()
    if number <= 1:
        print("Oops.... You should start with at least 2")
    else:
        result = check_if_prime_number(number)
        msg = f"{number} is {result}"

        print(msg)

main()

if __name__ == '__main__':
    assert check_if_prime_number(0) == -1
    assert check_if_prime_number(False) == -1
    assert check_if_prime_number("fgh") == -1