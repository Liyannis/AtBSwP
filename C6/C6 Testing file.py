"""
Chapter 6 string manipulation
testing file
"""

str1 = 'just some random text for testing'
str2 = 'more Random tExt, to T3S7'
str3 = 'TEXT'
str4 = 'Text'



def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)


ui = input('feed me ' )
if ui.isdecimal():
    print(type(ui))
print(ui)
