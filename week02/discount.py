import math
from datetime import datetime

# ANSI escaped sequences to print colored text to the terminal
white = '\x1b[1;37;40m'
blue = '\x1b[1;34;40m'

# Print a description of this program for the user to see.
print(blue + '\nthis program gets a customer\'s subtotal as input and if the subtotal is $50 or greater and today is Tuesday or Wednesday, the program must subtract 10 percentage from the subtotal.')

# Get the subtotal.
subtotal = float(input(white + 'Please enter the subtotal: '))

# Get the day of the week from the computer's operating system.
current_date_and_time = datetime.now()
# day_of_week = current_date_and_time.weekday()
day_of_week = 2

discount_amount = 0
additional_amount_to_get_discount = 0


if (day_of_week == 2 or day_of_week == 3):
        if (subtotal >= 50 ):
            discount_amount = subtotal*0.1
            subtotal = subtotal - discount_amount
        else: 
            additional_amount_to_get_discount = 50 - subtotal

sales_tax = subtotal*0.06
total = subtotal + sales_tax

if (discount_amount > 0):
    print(blue + f'Disccount Ammount: {discount_amount:.2f}')
else:
    print(blue + f'The additional amount the customer need to purchase to get discount : {additional_amount_to_get_discount:.2f}')
print(blue + f'Sales Tax Ammount: {sales_tax:.2f}')
print(blue + f'Total: {total:.2f}')