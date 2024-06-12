import pprint
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print('Total items: ', item_total)
    
items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(items)

print('Dragon Killed \nDragon loot: ')

def add_to_inventory(inventory, added_items):
    total_items = 0
    for k in added_items:
        if k not in inventory:
            inventory[k] = 1
        elif k in inventory:
            inventory[k] += 1
    for k, v in inventory.items():
        print(v, k)
        total_items += v
    print('Total items after loot: ', total_items)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(items, dragon_loot)