#H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.
hour=int(input())
minute=int(input())
second=int(input())
timeInSecond=(hour*3600)+(minute*60)+second
degree=(30/3600)*timeInSecond
print(degree)