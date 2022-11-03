"""
Demonstrate that numbers are passed to a function by value
and lists are passed to a function by reference.
"""
import json
import csv

def main():
    print("main()")
    periodic_table_list = make_periodic_table()
              
    print('# symbol: [name, atomic_mass]')              
    for item in periodic_table_list.items():
        key = item[0]
        value = item[1]        
        print(f'{key}: {value}')            


def make_periodic_table():         
    filename = 'table_of_elements.json'

    with open(filename) as json_file:
        periodic_table_list = json.load(json_file)
                  
    return periodic_table_list


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
