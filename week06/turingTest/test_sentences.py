"""
File: test_sentences.py
Author: Roberto Uriona
Purpose: Test the functions that generate sentences with four parts:
a determiner
a noun
a verb
a prepositional phrase
"""

import sentences 
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ['a', 'one', 'the']

    # This loop will repeat the statements inside it 4 times.
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
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = sentences.get_noun(1)

        # Verify that the single noun returned from get_noun
        # is one of the nouns in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ['birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'rabbits', 'women']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_nouns function which
        # should return a plural noun.
        word = sentences.get_noun(2)

        # Verify that the noun returned from get_noun
        # is one of the nouns in the plural_nouns list.
        assert word in plural_nouns

def test_get_verb():
    
    # 1. Test past tense verbs.

    past_tense_verbs = ['drank', 'ate', 'grew', 'laughed', 'thought', 'ran', 'slept', 'talked', 'walked', 'wrote']

    # This loop will repeat the statements inside it 4 times.    
    for _ in range(4):

        # Call the get_verb function which should return a verb in the past tense.
        word = sentences.get_verb(1, 'past')

        # Verify that the verb returned from get_verb
        # is one of the verbs in the past tense verbs list.
        assert word in past_tense_verbs

    # 2. Test single present verb tense.

    simple_present_tense_verbs = ['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs', 'sleeps', 'talks', 'walks', 'writes']


    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which should return a verb in the sinple present tense.
        word = sentences.get_verb(1, 'present')

        # Verify that the verb returned from get_verb
        # is one of the verbs in the simple present tense verbs list.
        assert word in simple_present_tense_verbs

    # 3. Test plural present verb tense.

    plural_present_tense_verbs = ['drink', 'eat', 'grow', 'laugh', 'think', 'run', 'sleep', 'talk', 'walk', 'write']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which should return a verb in the plural present tense.
        word = sentences.get_verb(2, 'present')

        # Verify that the verb returned from get_verb
        # is one of the verbs in the plural present tense verbs list.
        assert word in plural_present_tense_verbs

    # 4. Test future verb tense.

    future_tense_verbs = ['will drink', 'will eat', 'will grow', 'will laugh', 'will think', 'will run', 'will sleep', 'will talk', 'will walk', 'will write']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which should return a verb in the future tense.
        word = sentences.get_verb(1, 'future')

        # Verify that the verb returned from get_verb
        # is one of the verbs in the future tense verbs list.
        assert word in future_tense_verbs

def test_get_preposition():
    # 1. Test the prepositions.

    prepositions = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']

    # This loop will repeat the statements inside it 4 times.    
    for _ in range(4):

        # Call the get_preposition function which should return a preposition.
        word = sentences.get_preposition()

        # Verify that the verb returned from get_preposition
        # is one of the prepositions in the prepositions list.
        assert word in prepositions

def test_get_prepositional_phrase():    
    prepositions = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below','beyond', 'by', 
        'despite', 'except', 'for', 'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over', 'past', 'to', 'under', 
        'with', 'without']    
    single_determiners = ['a', 'one', 'the']
    plural_determiners = ['some', 'many', 'the']
    single_nouns = ['bird', 'boy', 'car', 'cat', 'child', 'dog',
        'girl', 'man', 'rabbit', 'woman']
    plural_nouns = ['birds', 'boys', 'cars', 'cats', 'children',
        'dogs', 'girls', 'men', 'rabbits', 'women']

    # 1. Test the single prepositional phrase.
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_prepositional_phrase function which
        # should return a single prepositional phrase.
        single_prepositional_phrase = sentences.get_prepositional_phrase(1)
        # Call split function to save each word belonging to preposition_phrase 
        # in the words list. 
        words = single_prepositional_phrase.split(' ')
        preposition = words[0]
        determiner = words[1]
        noun = words[2]

        # Test the number of words contained in words list.
        assert len(words) == 3                        
        # Test the preposition is in presitions list.
        assert preposition in prepositions
        # Test the determiner is in single_determiners list.
        assert determiner in single_determiners
        # Test the noun is in single_nouns list.
        assert noun in single_nouns

    # 2. Test the plural prepositional phrase.
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_prepositional_phrase function which
        # should return a plural prepositional phrase.
        plural_prepositional_phrase = sentences.get_prepositional_phrase(2)
        words = plural_prepositional_phrase.split(' ')
        preposition = words[0]
        determiner = words[1]
        noun = words[2]
        
        # Test the number of words contained in words list.
        assert len(words) == 3        
        # Test the preposition is in presitions list.
        assert preposition in prepositions
        # Test the determiner is in plural_determiners list.
        assert determiner in plural_determiners
        # Test the noun is in plural_nouns list.
        assert noun in plural_nouns

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])