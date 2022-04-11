# This is the unit test module of shopping basket project.
from functions.validity_check import validity_check
from functions.total_calculation import total_calculation
from functions.discount_calculation import discount_calculation
from functions.discount_setup import discount_setup


items_stock = ['Soup', 'Bread', 'Milk', 'Apples']
items_price = {'Soup': 0.65, 'Bread': 0.80, 'Milk': 1.30, 'Apples': 1.00}
items_discount = {'Apples': 10, 'Bread': 50}


def test_validity_check():
    # Verify the output of validity_check function
    items_basket = ['Apples', 'Bread', 'Orange']
    expected_output = False
    actual_output = validity_check(items_basket, items_stock)
    assert expected_output == actual_output

    items_basket = ['Apples', 'Bread', 'Soup']
    expected_output = True
    actual_output = validity_check(items_basket, items_stock)
    assert expected_output == actual_output


def test_discount_calculation():
    # Verify the output of discount_calculation function
    expected_output = 0.3
    actual_output = discount_calculation(1.00, 3, 10)
    assert expected_output == actual_output


def test_discount_setup():
    # Verify the output of discount_setup function
    items_basket = ['Apples', 'Milk']
    items_quantity = {'Apples': 2, 'Milk': 1}
    expected_output = 0.2
    actual_output = discount_setup('Apples', items_quantity, items_basket,
                                   items_price, items_discount)
    assert expected_output == actual_output

    items_basket = ['Soup', 'Bread']
    items_quantity = {'Soup': 2, 'Bread': 1}
    expected_output = 0.4
    actual_output = discount_setup('Bread', items_quantity, items_basket,
                                   items_price, items_discount)
    assert expected_output == actual_output

    items_basket = ['Soup', 'Bread']
    items_quantity = {'Soup': 3, 'Bread': 1}
    expected_output = 0.4
    actual_output = discount_setup('Bread', items_quantity, items_basket,
                                   items_price, items_discount)
    assert expected_output == actual_output

    items_basket = ['Soup', 'Bread']
    items_quantity = {'Soup': 4, 'Bread': 2}
    expected_output = 0.8
    actual_output = discount_setup('Bread', items_quantity, items_basket,
                                   items_price, items_discount)
    assert expected_output == actual_output


def test_total_calculation():
    # Verify the output of total_calculation function
    items_basket = ['Apples', 'Bread', 'Soup']
    items_quantity = {'Apples': 2, 'Bread': 2, 'Soup': 2}
    expected_subtotal = 4.90
    expected_discount_total = 0.60
    expected_total_price = 4.30
    expected_apples_discount_total = 0.20
    expected_bread_discount_total = 0.40
    actual_subtotal, actual_discount_total, actual_total_price, \
        actual_apples_discount_total, actual_bread_discount_total = \
        total_calculation(items_basket, items_price, items_quantity, items_discount)

    assert expected_subtotal == actual_subtotal
    assert expected_discount_total == actual_discount_total
    assert expected_total_price == actual_total_price
    assert expected_bread_discount_total == actual_bread_discount_total
    assert expected_apples_discount_total == actual_apples_discount_total
