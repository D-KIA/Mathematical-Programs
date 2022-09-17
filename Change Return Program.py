'''
The user enters a cost and then the amount of money given. The program will figure out the change and the number of
quarters, dimes, nickels, pennies needed for the change.

# Coins - Coins in India are presently being issued in denominations of one rupee, two rupees, five rupees and ten rupees
# Currency - Banknotes in India are currently being issued in the denomination of Rs 10, Rs 20, Rs 50, Rs 100, Rs 200,
  Rs 500 and Rs 2000.
'''
import pandas as pd
cost = abs(int(input('Enter Cost: Rs. ')))
paid = abs(int(input('Enter paid amount: Rs. ')))

change = abs(cost - paid)

curr_dict = {2000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

for k in curr_dict:
    if change == 0:
        break
    elif change - k >= 0:
        while change - k >= 0:
            curr_dict[k] += 1
            change = change - k
    if curr_dict[k] != 0:
        print(fr'''{curr_dict[k]} - Rs. {k} notes/coins''')