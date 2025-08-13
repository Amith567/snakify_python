#Given a three-digit number. Find the sum of its digits.
number=input()
sum=0
for num in number:
    sum+=int(num)
print(sum)