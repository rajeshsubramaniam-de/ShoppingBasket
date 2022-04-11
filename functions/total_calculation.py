# This module calculates all the total values needed in output.
from functions.discount_setup import discount_setup


def total_calculation(items_basket, items_price, items_quantity, items_discount):
    subtotal = 0
    discount_total = 0
    apples_discount_total = 0
    bread_discount_total = 0

    for item in items_basket:
        subtotal = (subtotal + (items_price[item] * items_quantity[item]))
        subtotal = round(subtotal, 2)

        if item in items_discount:
            discount_item_total = discount_setup(item, items_quantity, items_basket, items_price, items_discount)
            discount_total = discount_total + discount_item_total
            discount_total = round(discount_total, 2)
            if item == 'Apples':
                apples_discount_total = round(discount_item_total, 2)
            elif item == 'Bread':
                bread_discount_total = round(discount_item_total, 2)

    total_price = subtotal - discount_total
    total_price = round(total_price, 2)

    return subtotal, discount_total, total_price, apples_discount_total, bread_discount_total
