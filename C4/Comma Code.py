'''Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space,
with and inserted before the last item. For example, passing the previous
spam list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.'''

dr = dice_rolls = [3, 5, 6, 5, 5, 5, 6, 6, 5, 4, 5, 1, 2, 1, 1, 4, 6, 2, 3, 2]
spam = ['apples', 'bananas', 'tofu', 'cats']
ml = mixed_list = [3, 5, 6, 5, 'apples', 'bananas', 2.2]

def lpas(list): #list_print_as_string
    seperator=", "
    list_as_string = seperator.join(ltc(list)[:-1])
    print("The list you provided contains")
    print(list_as_string + " and " + str(list[-1]))


def ltc(list): #list_type_check
    new_list = []
    for item in list:
        if type(item) != str:
            new_list.append(str(item))
        else:
            new_list.append(item)
    return new_list


lpas(ml)