# Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.

number=int(input())
print("The next number for the number",number,"is {}.".format(number+1))
print("The previous number for the number",number," is {}.".format(number-1))