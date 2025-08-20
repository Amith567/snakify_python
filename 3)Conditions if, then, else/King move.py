# Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.


initial_x=int(input())
initial_y=int(input())
x=int(input())
y=int(input())
if initial_x==x:
    if initial_y==y or initial_y+1==y or initial_y-1==y:
        print("YES")
    else:
        print("NO")
elif initial_x-1==x:
    if initial_y==y or initial_y+1==y or initial_y-1==y:
        print("YES")
    else:
        print("NO")
elif initial_x+1==x:
    if initial_y==y or initial_y+1==y or initial_y-1==y:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
    
    