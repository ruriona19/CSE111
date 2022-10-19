import sentences 
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ['a', 'one', 'the']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = sentences.get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ['some', 'many', 'the']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = sentences.get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ['bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'rabbit', 'woman']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single determiner.
        single_noun = sentences.get_noun(1)

        # Verify that the single nount returned from get_determiner
        # is one of the nouns in the single_nouns list.
        assert single_noun in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ['birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'rabbits', 'women']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_nouns function which
        # should return a plural noun.
        plural_noun = sentences.get_noun(2)

        # Verify that the noun returned from get_noun
        # is one of the nouns in the plural_nouns list.
        assert plural_noun in plural_nouns

def test_get_verb():
    
    # 1. Test past verb tense.

    past_tense_verbs = ['drank', 'ate', 'grew', 'laughed', 'thought', 'ran', 'slept', 'talked', 'walked', 'wrote']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single determiner.
        verb = sentences.get_verb(1, 'past')

        # Verify that the single nount returned from get_determiner
        # is one of the nouns in the single_nouns list.
        assert verb in past_tense_verbs

    # 2. Test single present verb tense.

    simple_present_tense_verbs = ['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs', 'sleeps', 'talks', 'walks', 'writes']


    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_nouns function which
        # should return a plural noun.
        verb = sentences.get_verb(1, 'present')

        # Verify that the noun returned from get_noun
        # is one of the nouns in the plural_nouns list.
        assert verb in simple_present_tense_verbs

    # 3. Test plural present verb tense.

    plural_present_tense_verbs = ['drink', 'eat', 'grow', 'laugh', 'think', 'run', 'sleep', 'talk', 'walk', 'write']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_nouns function which
        # should return a plural noun.
        verb = sentences.get_verb(2, 'present')

        # Verify that the noun returned from get_noun
        # is one of the nouns in the plural_nouns list.
        assert verb in plural_present_tense_verbs

    # 4. Test future verb tense.

    future_tense_verbs = ['will drink', 'will eat', 'will grow', 'will laugh', 'will think', 'will run', 'will sleep', 'will talk', 'will walk', 'will write']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_nouns function which
        # should return a plural noun.
        verb = sentences.get_verb(1, 'future')

        # Verify that the noun returned from get_noun
        # is one of the nouns in the plural_nouns list.
        assert verb in future_tense_verbs

def test_get_preposition():
    # 1. Test the prepositions.

    prepositions = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single determiner.
        preposition = sentences.get_preposition()

        # Verify that the single nount returned from get_determiner
        # is one of the nouns in the single_nouns list.
        assert preposition in prepositions


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])