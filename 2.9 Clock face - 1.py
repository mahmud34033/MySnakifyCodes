# 2.9 Clock face - 1
## H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.


h=int(input())
m=int(input())
s=int(input())

print(h*30 + m*0.5 + s*0.00833333)