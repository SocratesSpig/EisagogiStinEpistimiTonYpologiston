import random

def show_grid(z):
    for line in z:
        board = ' '.join(str(X) for X in line)
        print (board)

def up(grid, X):
    return 1 if grid[X-10]=="*" else 0
def down(grid, X):
    return 1 if grid[X+10]=="*" else 0
def left(grid, X):
    return 1 if grid[X-1]=="*" else 0
def right(grid, X):
    return 1 if grid[X+1]=="*" else 0
def up_left(grid, X):
    return 1 if grid[X-11]=="*" else 0
def up_right(grid, X):
    return 1 if grid[X-9]=="*" else 0
def down_left(grid, X):
    return 1 if grid[X+9]=="*" else 0
def down_right(grid, X):
    return 1 if grid[X+11]=="*" else 0

mines = int(input("Enter number of mines(0-100): "))
while (mines < 0 or mines > 100):
    mines = input("ERROR: You have to give a number from 0 to 100!\nTry again: ")
var = [0]*(100-mines)
var += ["*"]*mines
random.shuffle(var)

for i in range(100):
    if var[i]==0:
        if i==0:
            var[i] += down(var,i) + right(var,i) + down_right(var,i)
        elif i==9:
            var[i] += down(var,i) + left(var,i) + down_left(var,i)
        elif i==90:
            var[i] += up(var,i) + right(var,i) + up_right(var,i)
        elif i==99:
            var[i] += up(var,i) + left(var,i) + up_left(var,i)
        elif i<9:
            var[i] += left(var,i) + down_left(var,i) + down(var,i) + down_right(var,i) + right(var,i)
        elif i>90:
            var[i] += left(var,i) + up_left(var,i) + up(var,i) + up_right(var,i) + right(var,i)
        elif i%10==0:
            var[i] += up(var,i) + up_right(var,i) + right(var,i) + down_right(var,i) + down(var,i)
        elif i%10==9:
            var[i] += up(var,i) + up_left(var,i) + left(var,i) + down_left(var,i) + down(var,i)
        else:
            var[i] += up(var,i) + down(var,i) + right(var,i) + left(var,i) + up_right(var,i) + \
                      down_right(var,i) + up_left(var,i) + down_left(var,i)

grid = []
for x in range(10):
    grid += [var[10*x:10*x+10]]

show_grid(grid)
