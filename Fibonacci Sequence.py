def f_seq(n = 0):
    series = [0, 1]
    sum = 0
    while True:
        sum = series[-2] + series[-1]
        if sum > n:
            break
        else:
            series.append(sum)
    return series
while True:
    num = input("Enter A Number: ")
    try:
        num = abs(int(num))
        break
    except:
        print("WRONG!!! IT'S NOT A Number You DUMASS")
print(f_seq(num))