# 3.8 Bishop moves
'''
In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.
The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.
'''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

a = x1-x2==0 and y1-y2==0
b = abs(x1-x2)==abs(y1-y2)

if a or b:
    print("YES")
else:
    print("NO")
