# 1.8 Two timestamps
'''
A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.
'''

t1h = int(input())
t1m = int(input())
t1s = int(input())
t2h = int(input())
t2m = int(input())
t2s = int(input())
sumh = (t2h-t1h)*3600
summ = (t2m-t1m)*60
sums = (t2s-t1s)

total = sumh+summ+sums

print(total)