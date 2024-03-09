# 2.8 Total cost
## A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.


a = int(input())
b = int(input())
n = int(input())

tc=a*100 + b
tp=n*tc
dollar=tp//100
cent=tp%100

print(dollar, cent)