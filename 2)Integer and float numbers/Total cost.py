#A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
priceDoller=int(input())
priceCent=int(input())
no=int(input())
totalPrice=(priceDoller*100+priceCent)*no
doller=totalPrice//100
cent=totalPrice%100
print(doller,str(cent).zfill(2))