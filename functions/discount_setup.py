# This module sets up all the values needed for discount calculation.
from functions.discount_calculation import discount_calculation


def discount_setup(item, items_quantity, items_basket, items_price, items_discount):
    discount_price = items_price[item]
    discount_percentage = items_discount[item]

    if (item == 'Bread') and \
            ('Soup' in items_basket) and \
            (items_quantity['Bread'] > 0) and \
            (items_quantity['Soup'] > 1):

        no_offer_for_soup = items_quantity['Soup'] // 2
        discount_quantity = 0
        while (discount_quantity != no_offer_for_soup) and (discount_quantity != items_quantity['Bread']):
            discount_quantity += 1
    elif item == 'Apples':
        discount_quantity = items_quantity[item]
    else:
        discount_quantity = 0

    discount_total = discount_calculation(discount_price, discount_quantity, discount_percentage)
    return discount_total
