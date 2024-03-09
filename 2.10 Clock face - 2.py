# 2.10 Clock face - 2
## Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.


s = input()

if s.find(".") >= 0:
    n = float(s)
else:
    n = int(s)

print((n%30)*12)