# A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
# The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

from math import ceil

classOne=int(input())
classTwo=int(input())
classThree=int(input())
oneBench=ceil(classOne/2)
twoBench=ceil(classTwo/2)
threeBench=ceil(classThree/2)
totalBench=oneBench+twoBench+threeBench
print(totalBench)