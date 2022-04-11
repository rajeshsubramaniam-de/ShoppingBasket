# This module calculates the discount amount.
def discount_calculation(discount_price, discount_quantity, discount_percentage):
    discount_amount = (discount_price * discount_quantity * discount_percentage) / 100
    discount_amount = round(discount_amount, 2)
    return discount_amount
