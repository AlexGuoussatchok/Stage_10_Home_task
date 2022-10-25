# Alex Goussatchok
# QA 4822
# Task: Heads or Tails
# v 1.0

# import random
#
# SIDE_1 = "head"
# SIDE_2 = "tail"
#
#
# def definition_of_tosses():  # we may use randomly generated number of coin tosses instead
#     tosses = int(input("Please input how many times do you want to toss the coin: "))
#     return tosses
#
#
# def count_coin_sides(tosses):
#     if isinstance(tosses, bool) or not isinstance(tosses, int):
#         return -1
#     else:
#         count_side_1 = 0
#         count_side_2 = 0
#         while tosses > 0:
#             i = random.randint(1, 2)
#             if i == 1:
#                 count_side_1 += 1
#             elif i == 2:
#                 count_side_2 += 1
#             tosses -= 1
#         return count_side_1, count_side_2
#
#
# def user_output(msg):
#     print(msg)
#
#
# def main():
#     tosses = definition_of_tosses()
#     if tosses == 0:
#         print("You forgot to toss the coin")
#     elif tosses < 0:
#         print("You couldn't do that")
#
#     else:
#         count_side_1, count_side_2 = count_coin_sides(tosses)
#         msg = f"The coin was tossed {tosses} times: {SIDE_1} felt out {count_side_1} times & {SIDE_2}" \
#               f" felt out {count_side_2} times"
#         user_output(msg)
#
#
# main()

#-------------------------------------------------------------------------------------------------------------------
# v 2.0 --> "for" loop

import random

SIDE_1 = "head"
SIDE_2 = "tail"


def definition_of_tosses():  # we may use randomly generated number of coin tosses instead
    tosses = int(input("Please input how many times do you want to toss the coin: "))
    return tosses


def count_coin_sides(tosses):
    if isinstance(tosses, bool) or not isinstance(tosses, int):
        return -1
    else:
        count_side_1 = 0
        count_side_2 = 0
        for tosses in range(tosses):
            i = random.randint(1, 2)
            if i == 1:
                count_side_1 += 1
            elif i == 2:
                count_side_2 += 1
            tosses -= 1
        return count_side_1, count_side_2


def user_output(msg):
    print(msg)


def main():
    tosses = definition_of_tosses()
    if tosses == 0:
        print("You forgot to toss the coin")
    elif tosses < 0:
        print("You couldn't do that")

    else:
        count_side_1, count_side_2 = count_coin_sides(tosses)
        msg = f"The coin was tossed {tosses} times: {SIDE_1} felt out {count_side_1} times & {SIDE_2}" \
              f" felt out {count_side_2} times"
        user_output(msg)


main()
