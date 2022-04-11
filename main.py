# This is the main module of shopping basket.
from functions.validity_check import validity_check
from functions.total_calculation import total_calculation


items_stock = ['Soup', 'Bread', 'Milk', 'Apples']
items_price = {'Soup': 0.65, 'Bread': 0.80, 'Milk': 1.30, 'Apples': 1.00}
items_discount = {'Apples': 10, 'Bread': 50}
items_quantity = {}


if __name__ == '__main__':

    while True:
        items_basket = input('PriceBasket ').split()
        items_basket = [item.capitalize() for item in items_basket]
        items_valid = validity_check(items_basket, items_stock)
        if items_valid:
            break

    for item in items_basket:
        items_quantity[item] = int(input(f'{item}_Quantity = '))

    subtotal, discount_total, total_price, apples_discount_total, bread_discount_total = \
        total_calculation(items_basket, items_price, items_quantity, items_discount)

    print(f'subtotal: £{subtotal:.2f}')

    if apples_discount_total > 0:
        print(f'Apples 10% off: £{apples_discount_total:.2f}')

    if bread_discount_total > 0:
        print(f'Bread 50% off with 2 Soup: £{bread_discount_total:.2f}')

    if discount_total > 0:
        print(f'discount_total: £{discount_total:.2f}')
    else:
        print('(No offers available)')

    print(f'total_price: £{total_price:.2f}')
