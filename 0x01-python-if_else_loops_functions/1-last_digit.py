#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
last_digit = number % 10
print(f"Last digit of {number:d} is {last_digit:d} ", end="")
if last_digit > 5:
    print(f"and is greater than 5")
elif last_digit == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
