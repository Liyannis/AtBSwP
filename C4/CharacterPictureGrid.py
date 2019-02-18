grid = [['0', '.', '.', '.', '.', '5'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['8', '.', '.', '.', '.', '.']]

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
for char in range(len(grid[0])):
    tempList = []
    for list in range(len(grid)):
        #print(char, list, grid[list][char])
        tempList.append(grid[list][char])
        if len(tempList) == len(grid):
            tempListStr=''
            print(tempListStr.join(tempList))