# Alex Goussatchok
# QA 4822
# Task: Try to guess a number
# v 1.0
# import random
#
#
# def mind_number():
#     number = random.randint(1, 100)
#     return number
#
#
# def user_input():
#     answer = int(input("Enter your number: "))
#     return answer
#
#
# def compare_numbers(answer, number):
#     while answer != number:
#         if answer > number:
#             print("The hidden number is smaller")
#         elif answer < number:
#             print("The hidden number is bigger")
#         answer = user_input()
#     else:
#         print("My congratulations")
#
#
# def main():
#     number = mind_number()
#     answer = user_input()
#     compare_numbers(answer, number)
#     again = input("Input 'q' for exit or hit 'ENTER' to play once again: ")
#     if again != "q":
#         main()
#     else:
#         exit()
#
#
# main()

# ======================================================================================================

# v 2.0
import random


def define_range():
    a = int(input("Enter a number for the hidden number range start: "))
    b = int(input("Enter a number for the hidden number range end: "))
    return a, b


def mind_number(a, b):
    number = random.randrange(a, b)
    return number


def user_input():
    answer = int(input("Enter your number: "))
    return answer


def compare_numbers(answer, number):
    for _ in range(4):
        if answer > number:
            print("The hidden number is smaller")
        elif answer < number:
            print("The hidden number is bigger")
        else:
            print("My congratulations!!!")
            break
        print(f"You have {4 - _} attempts left")
        answer = user_input()
    else:
        print(f"The hidden number was {number}.\nYou didn't guess my hidden number\nGAME OVER")



def main():
    a, b = define_range()
    number = mind_number(a, b)
    answer = user_input()
    compare_numbers(answer, number)
    again = input("Input 'q' for exit or hit 'ENTER' to play once again: ")
    if again != "q":
        main()
    else:
        exit()


main()
