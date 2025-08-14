# Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
if num_1 == num_2 == num_3 :
    print(3)
elif num_1 == num_2 or num_2 == num_3 or num_1 == num_3 :
    print(2)
else :
    print(0)