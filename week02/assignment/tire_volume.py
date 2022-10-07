# import the math module so I can use math.pi
import math 
# import datetime module to use datetime.now() function
from datetime import datetime

# Print a description of this program for the user to see.
print('\nThis program computes and outputs the volume of a car tire in the United States and stores the values entered in volumes.txt file\n')

# Assignment #1: Gets the current date from the computer's operating system.
current_date_and_time = datetime.now()


# Get the width of the tire in millimeters.
width = input('Enter the width of the tire in mm (ex 205): ')
# Get the aspect ratio of the tire.
aspect = input('Enter the aspect ratio of the tire (ex 60): ')
# Get the diameter of the wheel in inches.
diameter = input('Enter the diameter of the wheel in inches (ex 15): ')

# Converting string variables to integer.
w = int(width)
a = int(aspect)
d = int(diameter)

# Calculate the volume in liters.
v = (math.pi*math.pow(w,2))*a*(w*a + 2540*d)/10000000000

# Print the voulume of a car tire.
print('\nThe approximate volume is ' + f'{v:.2f} ' + 'liters\n')

# Exceeding the requiremens: Ask the user if she/he wants to buy tires with the dimensions that she/he entered.
buy_tires = input('Do you want to buy tires with the dimensions that you entered (yes/no)? ')
    
# Assignment #2: Opens a text file named volumes.txt for appending.
with open('volumes.txt', 'at') as volumes_file:

    # Assignment #3: Appends to the end of the volumes.txt file one line of text that contains the following five values:
        # current date
        # width of the tire
        # aspect ratio of the tire
        # diameter of the wheel
        # volume of the tire    
    if buy_tires == 'yes':
        # Exceeding the requirements: If the user answers "yes", ask for user´s full name and phone number and store that info in volumes.txt file.
        customer_name = input('Please enter your full name: ')
        customer_phone_number = input('Please enter your phone number: ')        
        print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {customer_name}, {customer_phone_number} ", file=volumes_file)
    else:        
        print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f} ", file=volumes_file)