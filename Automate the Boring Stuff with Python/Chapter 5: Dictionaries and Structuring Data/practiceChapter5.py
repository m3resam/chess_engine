# This function gets inventory_items keys and values and prints them in order.
def display_inventory(inventory):
    print('Inventory:')
    # Initialize total item counter
    item_total = 0
    # Loops trough the keys and values using the .items() method
    for k, v in inventory.items():
        # Print changing the order
        print(v, k)
        # Add the keys values to the total item counter
        item_total += v
    # Prints the total items
    print('Total items: ', item_total)

inventory_items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Calls the function dispaly_inventory taking as argument inventory_items
display_inventory(inventory_items)

print('Dragon Killed')

# This function gets both inventory_items(dictionary) and the dragin_loot(list) to add them together
def add_to_inventory(inventory, added_items):
    # Initialize total item counter
    total_items = 0
    # Loops through dragon_loot
    for k in added_items:
        # if k is not in inventory_items we add it as key at set a starting value of 1
        if k not in inventory:
            inventory[k] = 1
        # else if k is in inventory_items we add 1 to the exisiting value
        elif k in inventory:
            inventory[k] += 1
    # To avoid repetition, call display_inventory function to print the new inventory with the wanted order
    display_inventory(inventory)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inventory_items, dragon_loot)
