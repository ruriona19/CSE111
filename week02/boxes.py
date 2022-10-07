# import the math module so I can use math.pi
import math

# ANSI escaped sequences to print colored text to the terminal
white = '\x1b[1;37;40m'
blue = '\x1b[1;34;40m'

# Print a description of this program for the user to see.
print(blue + '\nThis program computes and outputs the size of a car tire in the United States\n')

# Get the number of items.
number_items = input(white + 'Enter the number of items: ')
# Get the number of itmes per box.
number_items_per_box = input('Enter the number of items per box: ')


# Computes and print the number of boxes necessary to hold the items.
number_of_necessary_boxes = math.ceil(int(number_items)/int(number_items_per_box))

print(blue + f'\nFor {number_items} items, packing {number_items_per_box} items in each box, you will need {number_of_necessary_boxes} boxes')