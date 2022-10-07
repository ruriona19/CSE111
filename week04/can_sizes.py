"""Compute and print the volume of a right circular cone."""

# Import the standard math module so that
# math.pi can be used in this program.
import math
import csv


def main():
    # Get the list of can sizes from csv file
    steel_can_sizes = get_list_of_can_sizes('steel_can_sizes.csv')
    name_index = 0
    radius_index = 1
    height_index = 2 
       

    for steel_can_size in steel_can_sizes:
        name = steel_can_size[name_index]
        radius = float(steel_can_size[radius_index])
        height = float(steel_can_size[height_index])

        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        storage_efficiency = volume/surface_area
        print(f'{name} -> {storage_efficiency:.2f}')

def get_list_of_can_sizes(filename):
    """Get a list of can sizes from csv file and save them in steel_can_sizes list

    Parameters
        filename: The name of the csv file to read from.        
    Return: The list of can sizes.
    """ 
    steel_can_sizes = []

    with open(filename) as steel_can_sizes_file:
        csvreader = csv.reader(steel_can_sizes_file)
        next(csvreader)
            
        for steel_can_size in csvreader:        
            steel_can_sizes.append(steel_can_size)
    return steel_can_sizes

def compute_surface_area(radius, height):        
    surface_area = 2*math.pi*radius*(radius + height)

    return surface_area

def compute_volume(radius, height):          
    volume = math.pi*math.pow(radius,2)*height

    return volume

# Start this program by
# calling the main function.
main()