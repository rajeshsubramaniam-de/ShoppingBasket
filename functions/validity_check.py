# This module checks whether all the items in the basket are valid.
def validity_check(items_basket, items_stock):
    items_valid = True
    for item in items_basket:
        if item not in items_stock:
            print('Please check available items and enter in correct format')
            print(f'Available Items: {items_stock}')
            items_valid = False
            break
    return items_valid
