# Find e to the Nth Digit - Just like the previous problem, but with e instead of π (pi). Enter a number and have the
# program generate e up to that many decimal places. Keep a limit to how far the program will go.
import math
from math import e


def e_with_precision(n):
    return '%.*f' % (n, e)


# Works for upto 51 decimal places

while True:
    # ask until you get correct input
    print('Precision must be between 1 and 51')
    precision = int(input('Number of decimal places: '))
    if 51 >= precision > 0:
        break
print(e_with_precision(precision))