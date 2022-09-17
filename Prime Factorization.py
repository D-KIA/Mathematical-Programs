# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
while True:
    try:
        ask = input('Do you want to Check prime number(1) or Find prime factors(2): ')
        if ask not in ('1', '2'):
            raise
        num = int(input('Enter a Number: '))
        break
    except:
        print('Wrong Input!!!! Do it again')

# To find Factors
def factors(num):
    list = []
    while num % 7 == 0:
        list.append(7)
        num = num/7
    while num % 5 == 0:
        list.append(5)
        num = num/5
    while num % 3 == 0:
        list.append(3)
        num = num / 3
    while num % 2 == 0:
        list.append(2)
        num = num / 2
    if num != 1:
        list.append(int(num))
    return list

# To check Prime
def prime(num):
    for x in range(2, num):
        if num % x == 0:
            return f'{num} is NOT a prime number'
    return f'{num} is a prime number'


if ask == '1':
    print(prime(num))
else:
    print(factors(num))