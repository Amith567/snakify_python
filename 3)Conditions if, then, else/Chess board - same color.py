# Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

initial_x=int(input())
initial_y=int(input())
final_x=int(input())
final_y=int(input())

if initial_x%2 == final_x%2:
    if initial_y%2 == final_y%2:
        print("YES")
    else:
        print("NO")
else:
    if initial_y%2 != final_y%2:
        print("YES")
    else:
        print("NO")