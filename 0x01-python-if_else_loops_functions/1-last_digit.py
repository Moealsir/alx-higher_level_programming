#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
p1 = "Last digit of {} is {} and is less than 6 and not 0"
p2 = "Last digit of {} is {} and is greater than 5"
if last_digit < 1:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
elif 1 > last_digit < 6:
    print(p1.format(number, last_digit))
else:
    print(p2.format(number, last_digit))
