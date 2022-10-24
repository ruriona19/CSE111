"""
Demonstrate that numbers are passed to a function by value
and lists are passed to a function by reference.
"""
import random
import csv

def main():
    print("main()")
    periodic_table_list = make_periodic_table()
    periodic_table_list.index
    for element in periodic_table_list:
        print(f'{element[1]}  {element[2]}')


def make_periodic_table():     
    filename = 'table_of_elements.csv'
    periodic_table_list = []


    with open(filename) as table_of_elemnts_file:
        csvreader = csv.reader(table_of_elemnts_file)
        next(csvreader)
            
        for element in csvreader:
            atomicMass = element[2]
            element[2] = float(atomicMass)
            periodic_table_list.append(element)
    return periodic_table_list



# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
