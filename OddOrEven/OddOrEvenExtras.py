# ######################################################
#
# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#
# OddOrEvenExtras.py
#
# ######################################################
#
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd
# number react differently when divided by 2?
#
# Extras:
#
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#
# ######################################################

print("Testing if a number is odd or even")
user_input = int(input("Enter a number: "))

if user_input % 4 == 0:
    print("This is a multiple of 4!")

if user_input % 2 == 0:
    print("Even!")
else:
    print("Odd!")
