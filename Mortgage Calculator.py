'''
Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
Also figure out how long it will take the user to pay back the loan.
For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
-A fixed-rate mortgage is a home loan with a fixed interest rate for the entire term of the loan.
-Once locked in, the interest rate does not fluctuate with market conditions.
'''
def monthly_amount(interest, lone_amount, term):
    for c in range(0, term):
        lone_amount = lone_amount + lone_amount * interest
    return round(lone_amount/term)

def month_count(lone_amount, pay_per_month, interest):
    left_amount = lone_amount
    count = 0
    while left_amount > 0:
        left_amount = left_amount + left_amount * interest
        left_amount = left_amount - pay_per_month
        count += 1
    return count

choice = ''
print('''What do you want to calculate:-
               A : How much would you have to pay monthly
               B : Count the months do you have pay
      ''')
while choice not in ('A', 'B'):
    choice = input('Type "A" or "B" : ')

if choice == 'A':
    while True:
        try:
            lone_amount = abs(float(input('Enter Lone Amount: ')))
            term = abs(int(input('Enter Term in years: '))) * 12
            interest = (abs(float(input('Enter Monthly Interest: ')))) / 100
            break
        except:
            continue
    print(monthly_amount(interest, lone_amount, term))

elif choice == 'B':
    while True:
        try:
            lone_amount = abs(float(input('Enter Lone Amount: ')))
            interest = (abs(float(input('Enter Monthly Interest: '))))/100
            pay_per_month = abs(float(input('Enter Amount You  Will Be Paying Per Month: ')))
            break
        except:
            continue

    print(month_count(lone_amount, pay_per_month, interest))