# 3.9 Queen move
'''
Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.
'''

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

rock = (x1==x2) or (y1==y2)
bishop = abs(x1-x2)==abs(y1-y2)

if rock or bishop:
    print("YES")
else:
    print("NO")