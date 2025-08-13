# A timestamp is three numbers: a number of hours, minutes and seconds.
#  Given two timestamps, calculate how many seconds is between them.
#  The moment of the first timestamp occurred before the moment of the second timestamp.



firstHour=int(input())
firstMinute=int(input())
firstSecond=int(input())
secondHour=int(input())
secondMinute=int(input())
secondSecond=int(input())
firstTime=(firstHour*60*60)+(firstMinute*60)+firstSecond
secondTime=(secondHour*60*60)+(secondMinute*60)+secondSecond
diffTime=secondTime-firstTime
print(diffTime)
