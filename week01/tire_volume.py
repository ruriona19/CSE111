# import the math module so I can use math.pi
import math as m

# ANSI escaped sequences to print colored text to the terminal
white = '\x1b[1;37;40m'
blue = '\x1b[1;34;40m'

# Print a description of this program for the user to see.
print(blue + '\nThis program computes and outputs the size of a car tire in the United States\n')

# Get the width of the tire in millimeters.
width = input(white + 'Enter the width of the tire in mm (ex 205): ')
# Get the aspect ratio of the tire.
aspect = input('Enter the aspect ratio of the tire (ex 60): ')
# Get the diameter of the wheel in inches.
diameter = input('Enter the diameter of the wheel in inches (ex 15): ')

# converting string variables to integer
w = int(width)
a = int(aspect)
d = int(diameter)

# Calculate the volume in liters.
v = (m.pi*m.pow(w,2))*a*(w*a + 2540*d)/10000000000

print(blue + '\nThe approximate volume is ' + white + f'{v:.2f} ' + blue + 'liters\n')