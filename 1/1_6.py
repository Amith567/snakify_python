# N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?

student=int(input())
apple=int(input())
apple_used=apple//student
apple_remaining=apple%student
print(apple_used)
print(apple_remaining)