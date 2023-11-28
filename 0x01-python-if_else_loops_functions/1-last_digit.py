#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
p0 = "Last digit of {} is {} and is 0"
pp = "Last digit of {} is -{} and is less than 6 and not 0"
pn = "Last digit of {} is {} and is less than 6 and not 0"
pg = "Last digit of {} is {} and is greater than 5"
if last_digit == 0:
    print(p0.format(number, last_digit))
elif last_digit < 6 and last_digit != 0:
    if last_digit < 0:
        print(pp.format(number, last_digit))
    else:
        print(pn.format(number, last_digit))
else:
    print(pg.format(number, last_digit))
