# Import the csv module so that it can be used
# to read from the accidents.csv file.
import csv
from datetime import datetime


# Column numbers from the products.csv file.
PRODUCT_NUMBER_COLUMN = 0
PRODUCT_NAME_COLUMN = 1
PRODUCT_PRICE_COLUMN = 2


# Column numbers from the request.csv file.
REQUEST_PRODUCT_NUMBER_COLUMN = 0
QUANTITY_COLUMN = 1


def main():

    try:
        sales_tax_rate = 0.06 
        number_of_items = 0
        sub_total = 0.0
        sales_tax = 0
        current_date_and_time = datetime.now()

        # Prompt the user for a filename and open that text file.
        products_dict = read_dict('products.csv', PRODUCT_NUMBER_COLUMN)
        
        print('Inkom Emporium')
        #print(products_dict)

        with open("request.csv", "rt") as request_file:

            reader = csv.reader(request_file)
            next(reader)

            print()
            print('Requested Items')

            # Read each row in the CSV file one at a time.
            # The reader object returns each row as a list.
            for row_list in reader:

                # For the current row, retrieve the
                # values in columns 0, 3, and 4.
                product_number_key = row_list[REQUEST_PRODUCT_NUMBER_COLUMN]
                request_quantity = int(row_list[QUANTITY_COLUMN])
                product_details = products_dict[product_number_key]
                product_name = product_details[PRODUCT_NAME_COLUMN]
                product_price = float(product_details[PRODUCT_PRICE_COLUMN])

                number_of_items += request_quantity
                sub_total += product_price*request_quantity

                print(f'{product_name}: {request_quantity} @ {product_price}')
            
        sales_tax = sub_total*sales_tax_rate
        total = sales_tax + sub_total

        print()
        print(f'Number of Items: {number_of_items}')
        print(f'Subtotal: {sub_total:.2f}')
        print(f'Sales Tax: {sales_tax:.2f}')
        print(f'Total: {total:.2f}')   
        print()
        print('Thank you for shopping at the Inkom Emporium')   
        print(f'{current_date_and_time:%a %b %d %I:%M:%S %Y}')
        
    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)
    except KeyError as key_err:
        print(f'Error: unknown product ID in the request.csv file {key_err}' )    


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary

# If this file was executed like this:
# > python accidents.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()

