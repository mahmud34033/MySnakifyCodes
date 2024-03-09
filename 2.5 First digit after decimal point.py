# 2.5 First digit after decimal point
## Given a positive real number, print its first digit to the right of the decimal point.

n = float(input())
print(int(n*10)%10)