grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

'''You can think of grid[x][y] as being the character at the x- and y-coordinates
of a “picture” drawn with text characters.
The (0, 0) origin will be in the upper-left
corner, the x-coordinates increase going right,
and the y-coordinates increase going down.
Copy the previous grid value, and write code that uses it to print the image.
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....'''

################################################################################
# https://www.youtube.com/watch?v=wX7G6QLiPk8
# https://youtu.be/XbWj0SkhWGo
# https://youtu.be/uWBz_R8pNy4

for x,y in grid([len(grid)], len(grid[1])):
    print(len(x[0]))


#def rotate_clockwise_90():
#tempList = []
#for x in grid:
#    for y in grid:
#        tempList.append(y)
    


grid = [['0', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['8', '.', '.', '.', '.', '.']]

'''
first i need to loop through grid[8-0]
while in that loop i need to grab only the first item from the list
append that to a temp list
grid[8][0]
grid[x][y]
'''
x = reversed(range(len(grid)))
y = range(len(grid[0]))

for p in x:
  #print(grid[r])
  for i in grid[p]:
    print(i)

  

'''
for li in reversed(range(len(grid))): #listindex
    tl=[] #templist
    for char in grid[li]:
        #print(char)
        tl.append(char)
        print(tl)
        
    turnedGrid=[]
    turnedGrid.append(tl)
print(turnedGrid)
'''
# teat at home

for char in range(len(grid[0])):
    for list in range(len(grid)):
        print(char, list)
        print(grid[list][char])
