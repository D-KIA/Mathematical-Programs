'''
Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
'''
'''
How to convert binary to decimal
For binary number with n digits:

dn-1 ... d3 d2 d1 d0

The decimal number is equal to the sum of binary digits (dn) times their power of 2 (2n):

decimal = d0×2^0 + d1×2^1 + d2×2^2 + ...
'''

def b2d(binary):
    decimal = 0
    index = 1
    for n in binary:
        decimal = decimal + int(n) * (2 ** (len(binary)-index))
        index += 1
    return decimal


'''
How to convert decimal to binary
Conversion steps:
Divide the number by 2.
Get the integer quotient for the next iteration.
Get the remainder for the binary digit.
Repeat the steps until the quotient is equal to 0.
'''
def d2b(decimal):
    print(decimal)
    q = decimal
    r = []
    while q != 0:
        r.append(q % 2)
        q = q // 2
    return r


while True:
    try:
         print('''
                            1 : Convert Decimal to Binary
                            2 : Convert Binary to Decimal
                ''')
         task = input('Pick the task (1/2) : ')
         if task in ('1', '2'):
            break
    except:
        continue

if task == '1':
    while True:
        try:
            decimal = int(input('Enter decimal: '))
            ans = d2b(decimal)
            for i in ans:
                print(i, end='')
            break
        except:
            continue

if task == '2':
    while True:
        clist = []
        binary = input('Enter binary: ')
        for n in binary:
            if n not in clist:
                clist.append(n)
        if clist == ['1', '0'] or clist == ['0', '1']:
            break
        else:
            continue
    print(b2d(binary))