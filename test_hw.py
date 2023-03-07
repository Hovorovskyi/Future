inv_count = {}
inv_zmist = {}


def start():
    print("""\nYou can do this:
    1 - check inventory
    2 - append new item
    3 - delete item
    4 - update inventory
    5 - search item
    q - quit from prog
    """)
    enter_client = input('If you want to do something, enter the number: ')
    return check_enter_client(enter_client)


def check_enter_client(enter):
    if enter == '1':
        return check_inventory()
    elif enter == '2':
        return append_new_item()
    elif enter == '3':
        return delete_item()
    elif enter == '4':
        return update_inventory()
    elif enter == '5':
        search_item()
    elif enter.lower() == 'q':
        print('Have a good day.')
    else:
        print('\nPlease, enter one of this list.')
        return start()


def check_inventory():
    for j, k in inv_zmist.items():
        if j in inv_count:
            print(f'\nItem: {j}. \nRemainder: {inv_count[j]}.')
        print(f'Description: {k}.\n')
    return start()


def append_new_item():
    item = input('Enter name of item: ')
    count = int(input('Enter how much product you append: '))
    zmist = input('Enter description: ')
    inv_count[item] = count
    inv_zmist[item] = zmist
    return start()


def delete_item():
    item = input('Enter name of item: ')
    if item in inv_count:
        print(f"{item} is delete.")
        inv_count.pop(item)
        inv_zmist.pop(item)
    else:
        print('\nThis item not in your inventory.')
    return start()


def update_inventory():
    item = input('Enter name of item for update: ')
    count = int(input('Enter how much product you append: '))
    if item not in inv_count:
        print('''\nThis item not in your inventory.
        Enter item that is in inventory.''')
        return start()
    inv_count[item] = count
    return start()


def search_item():
    check = input('Enter name of item or description: ')
    for j, k in inv_zmist.items():
        if check.lower() in j.lower() or check.lower() in k.lower():
            if j in inv_count:
                if check.lower() in j.lower():
                    print(f'\nItem: {j}. Remainder: {inv_count[j]}.')
            print(f'Description: {k}.\n')
        else:
            print('No items in.')
    return start()


if __name__ == '__main__':
    client = start()
