import csv


def main():    
    # Read the contents of the students.csv into a
    # dictionary named studentss_dict. Use
    # the I-Number as the keys in the dictionary.
    students_dict = read_dict("students.csv")

    # Print the students dictionary.
    print(students_dict)
    
    # Get the student name given an i_number
    i_number = input('Please enter an I-Number (xxxxxxxx): ')
    student_name = get_student_name(i_number, students_dict)
    print(student_name)

    # Strech Challenge
    # Code to remove dashes from the I-Number that the user enters.
    i_number = input('Please enter an I-Number with dashes(xx-xxx-xxx): ')
    i_number_without_dashes = i_number.replace('-','')
    student_name = get_student_name(i_number_without_dashes, students_dict)
    print(student_name)


def read_dict(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """    
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1    
    dictionary = {}
    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[I_NUMBER_INDEX]
                dictionary[key] = row_list[NAME_INDEX]
    
    return dictionary

def get_student_name(i_number, students_dict):
        
    if students_dict.get(i_number) is not None:
        return students_dict[i_number]
    else:
        return 'No such student'


# Call main to start this program.
if __name__ == "__main__":
    main()