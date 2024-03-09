# 2.3 Sum of digits
## Given a three-digit number. Find the sum of its digits.

s=input()
sum=0
for x in s:
  sum+=int(x)

print(sum)