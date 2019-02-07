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
    


#rotate_clockwise_90()