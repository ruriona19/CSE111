from ast import If
import random

def main():
    print_introductory_text()
    statements = ['I feel that I am a person of worth, at least on an equal plane with others.',
                 'I feel that I have a number of good qualities.',
                 'All in all, I am inclined to feel that I am a failure.',
                 'I am able to do things as well as most other people.',
                 'I feel I do not have much to be proud of.',
                 'I take a positive attitude toward myself.',
                 'On the whole, I am satisfied with myself.',
                 'I wish I could have more respect for myself.',
                 'I certainly feel useless at times.',
                 'At times I think I am no good at all.']
   
    total_score = 0
    positive_statement_indexes = [0,1,3,5,6]
    for i in range(10):
        print(statements[i])
        answer = get_valid_response()
        if positive_statement_indexes.count(i) > 0:
            is_positive_statement = True
        else:
            is_positive_statement = False
        response_score = compute_response_score(answer, is_positive_statement)
        total_score += response_score
    
    print(f'Your score is {total_score}.')
    print('A score below 15 may indicate problematic low self-esteem.')
    

def print_introductory_text():
    """Print the introductory text.

    Parameter: None
    Return: None
    """
    introductory_text = """
    This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:

    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.
    """
    print(introductory_text)

def get_valid_response():
    """Asking the user for input until they give a valid response.
    Parameter: None
    Return: Valid response
    """
    while True:
        response = input('Enter D, d, a, or A: ')
        if response == 'D' or response == 'd' or response == 'a' or response == 'A':
            break
        else:  
            print('Please enter a valid answer.')
            continue

    return response

def compute_response_score(answer, is_positive_statement):
    """Asking the user for input until they give a valid response.
    Parameter: None
    Return: Valid response
    """
    if is_positive_statement:
        if answer == 'D': 
            return 0
        elif answer == 'd': 
            return 1 
        elif answer == 'a': 
            return 2
        elif answer == 'A': 
            return 3
    else:
        if answer == 'D': 
            return 3
        elif answer == 'd': 
            return 2 
        elif answer == 'a': 
            return 1
        elif answer == 'A': 
            return 0

if __name__ == "__main__":
    main()