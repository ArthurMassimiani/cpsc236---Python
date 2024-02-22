TAX_RATE = 0.06

def calculate_sales_tax(total_cost):
    return round(total_cost * TAX_RATE, 2)

def calculate_total_after_tax(total_cost, sales_tax):
    return round(total_cost + sales_tax, 2)