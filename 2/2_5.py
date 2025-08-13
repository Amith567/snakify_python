#Given a positive real number, print its first digit to the right of the decimal point.
number=float(input())
num=number-int(number)
print(str(num)[2])