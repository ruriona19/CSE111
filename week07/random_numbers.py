"""
Demonstrate that numbers are passed to a function by value
and lists are passed to a function by reference.
"""
import random

def main():
    print("main()")
    numbers = [16.2, 75.1, 52.3]
    print(f"Numbers list: {numbers}")
    append_random_numbers(numbers)
    print(f"Numbers list after call append_random_numbers with one parameter:")
    print(numbers)
    append_random_numbers(numbers, 3)
    print(f"Numbers list after call append_random_numbers with two parameter:")
    print(numbers)

    words = []
    append_random_words(words, 3)
    print(f"Words list after call append_random_words with two parameter:")
    print(words)


def append_random_numbers(numbers_list, quantity=1):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    
    for i in range(0, quantity):
        number = round(random.uniform(0.0,100.0), 1)
        numbers_list.append(number)


def append_random_words(words_list, quantity=1):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    fruits = ['apple', 'orange', 'limon', 'watermelon', 'tandarin','pineapple']
    for i in range(0, quantity):
        random_index = random.randrange(5)
        words_list.append(fruits[random_index])

    


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
