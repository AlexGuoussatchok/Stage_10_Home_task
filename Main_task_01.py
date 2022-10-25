# Alex Goussatchok
# QA 4822
# Task: greatest common divisor & least common multiple
# v 1.0

def user_input():
    num_1 = int(input("Please enter the first number: "))
    num_2 = int(input("Please enter the second number: "))
    return num_1, num_2


def find_gcd(num_1, num_2):
    gcd = 1  # gcd --> greatest common divisor
    for i in range(1, num_1 + 1):
        for j in range(1, num_1 + 1):
            if i * j == num_1 and num_2 % i == 0:
                if i > gcd:
                    gcd = i
    return gcd


def least_common_multiple(num_1, num_2):
    lcm = [] # --> least common multiple
    for i in range(1, num_1 + 1):
        for j in range(1, num_2):
            if i * num_1 == j * num_2:
                lcm.append(i * num_1)
    return min(lcm)


def use_output(msg):
    print(msg)


def main():
    num_1, num_2 = user_input()
    gcd = find_gcd(num_1, num_2)
    lcm = least_common_multiple(num_1, num_2)
    msg = f"For numbers {num_1} and {num_2}: greatest common divisor is {gcd} & the least common multiple is {lcm}"
    use_output(msg)


main()
