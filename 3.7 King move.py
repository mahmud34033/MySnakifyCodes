# 3.7 King move
'''
Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.
'''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

a = x1==x2 and (y1-1 == y2 or y1+1 == y2)
b = y1==y2 and (x1-1 == x2 or x1+1 == x2)
c = x1+1 == x2 and y1+1 == y2
d = x1-1 == x2 and y1-1 == y2
e = x1-1 == x2 and y1+1 == y2
f = x1+1 == x2 and y1-1 == y2

if a or b or c or d or e or f:
    print("YES")
else:
    print("NO")
