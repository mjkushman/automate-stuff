#inventory.py

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        #print (str(k) + ': '+ str(v))
        print ('{}: {}'.format(k,v))
        item_total = item_total + v
    print()
    print('Total items: {}'.format(item_total))
    print()

#displays inventory of stuff
#displayInventory(stuff)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'diamond', 'ruby','sultry woman']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    print('Added items to inventory')


#displays inventory of inv
displayInventory(inv)

#Adds dragonloot to inv
addToInventory(inv, dragonLoot)

#displays inventory of inv
displayInventory(inv)

