# pi finder function
def pi_finder(n):
    p = 22/7
    return f'{p:.{n+1}}'

# Asking for number
while True:
    try:
        number = int(input('Please enter a integer (0 to 51): '))
        if number not in  range(0, 51):
            print("Out of range")
            continue
        else:
            break
    except:
        print("please enter a number between 0 to 51")
        continue

ans = pi_finder(number)
print(ans)