from datetime import datetime

current_date_and_time = datetime.now()
# Requirement 1: Get the day of the week from computer's operating system.
day_of_the_week = current_date_and_time.weekday()

subtotal = float(input('Please enter the subtotal:'))

if (day_of_the_week == 1 or day_of_the_week == 2):
    if (subtotal >= 50): 
        # Requirement 2: Compute and print the discount amount if applicable.       
        discount_amount = subtotal*0.1
        subtotal -= discount_amount
        print(f'Disccount Ammount: {discount_amount:.2f}')
    else: 
        # First strech challenge
        additional_amount_to_get_discount = 50 - subtotal
        print(f'The additional amount the customer need to purchase to get discount : {additional_amount_to_get_discount:.2f}')
    
# Requirement 3: Compute and print the sales tax amount and the total amount due.    
sales_tax = subtotal*0.06
total = subtotal + sales_tax
print(f"Sakes Tax Ammount: {sales_tax:.2f}")
print(f"Total: {total:.2f}")








