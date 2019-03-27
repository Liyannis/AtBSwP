'''
You are creating a fantasy video game. The data structure to model the player’s
inventory will be a dictionary where the keys are string values describing the
item in the inventory and the value is an integer value detailing how many of
that item the player has.
For example,
the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.
Write a function named displayInventory() that would take
any possible “inventory” and display it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger

Total number of items: 62
'''
################################################################################
from random import randint
#import prettyprint 


playerInventory = {}

#lootTable = ['Gold Coin', 'Silver Coin', 'Copper Coin',
#             'Torch', 'Arrow', 
#             ] 

lootTableMax = {'Gold Coin': 10, 'Silver Coin': 15, 'Copper Coin': 20,
             'Torch': 2, 'Arrow': 5, 
             }

#def displayInventory():
    
droppedLoot = {}
droppedNumberOfLootItems = 3 #randint(0, len(lootTableMax))
#print(droppedNumberOfLootItems)#for debugging


for n in range(droppedNumberOfLootItems):
    droppedItem = list(lootTableMax.keys())[randint(0, len(lootTableMax)-1)]
    amount = randint(0, lootTableMax[droppedItem])
    if droppedItem not in droppedLoot:
        droppedLoot[droppedItem] = amount
    else:
        break
    
if len(droppedLoot) == 0:
    print('sorry ' + str(len(droppedLoot)) + ' drops')
else:
    print(str(len(droppedLoot)) + ' drops')

print('you pick up the items')
#print(droppedLoot)
print('press anything to keep going?')
print('or just press enter to exit')
