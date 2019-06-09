'''
Write a function named displayInventory() that would take any possible
“inventory” and display it in a column with item's count and item's name
along with the total number of items.
Also write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary and the addedItems parameter is a list.
The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the
same item.
'''

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'parchment': 2}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'parchment']


def add_to_inventory(inv, added_items):
    for v in added_items:
        inv.setdefault(v, 0) # inserting list values into dictionary under 0 count if not exists, otherwise +1
        inv[v] += 1
    return inv

def display_inventory(inv):
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))


new_inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(new_inventory)

