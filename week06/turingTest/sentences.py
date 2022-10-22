"""
File: sentences.py
Author: Roberto Uriona
Purpose: Generate sentences with four parts:
a determiner
a noun
a verb
a prepositional phrase
"""

import random

def main():
    sentence = make_sentence(1,'past')
    print(f'Single-Past sentence: {sentence}')

    sentence = make_sentence(1,'present')
    print(f'Single-Present sentence: {sentence}')

    sentence = make_sentence(1,'future')
    print(f'Single-Future sentence: {sentence}')

    sentence = make_sentence(2,'past')
    print(f'Plural-Past sentence: {sentence}')

    sentence = make_sentence(2,'present')
    print(f'Plural-Present sentence: {sentence}')

    sentence = make_sentence(2,'future')
    print(f'Plural-Future sentence: {sentence}')

    print('=============================Exceeding the Requirements================================')

    sentence = make_sentence_with_two_prepositional_phrase(1,'past')
    print(f'Single-Past sentence: {sentence}')

    sentence = make_sentence_with_two_prepositional_phrase(1,'present')
    print(f'Single-Present sentence: {sentence}')

    sentence = make_sentence_with_two_prepositional_phrase(1,'future')
    print(f'Single-Future sentence: {sentence}')

    sentence = make_sentence_with_two_prepositional_phrase(2,'past')
    print(f'Plural-Past sentence: {sentence}')

    sentence = make_sentence_with_two_prepositional_phrase(2,'present')
    print(f'Plural-Present sentence: {sentence}')

    sentence = make_sentence_with_two_prepositional_phrase(2,'future')
    print(f'Plural-Future sentence: {sentence}')    


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ['a', 'one', 'the']
    else:
        words = ['some', 'many', 'the']

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ['bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl',
                 'man', 'rabbit', 'woman']
    else:
        nouns = ['birds', 'boys', 'cars', 'cats', 'children', 'dogs',
                 'girls', 'men', 'rabbits', 'women']

    # Randomly choose and return a determiner.
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 'past':
        verbs = ['drank', 'ate', 'grew', 'laughed', 'thought', 'ran',
                 'slept', 'talked', 'walked', 'wrote']
    elif tense == 'present' and quantity == 1:
        verbs = ['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs',
                 'sleeps', 'talks', 'walks', 'writes']
    elif tense == 'present' and quantity != 1:
        verbs = ['drink', 'eat', 'grow', 'laugh', 'think', 'run', 'sleep',
                 'talk', 'walk', 'write']
    elif tense == 'future':
        verbs = ['will drink', 'will eat', 'will grow', 'will laugh',
                 'will think', 'will run', 'will sleep', 'will talk', 'will walk', 'will write']

    # Randomly choose and return a determiner.
    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']

    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    prepositional_phrase = get_preposition() + ' ' + get_determiner(quantity) + ' ' + get_noun(quantity) 
    return prepositional_phrase

def make_sentence(quantity, verb_tense):
    """Calls get_determiner, get_noun, get_verb, and get_prepositional_phrase functions and 
       builds and return a sentence.

    Parameter
        quantity: an integer.
            If quantity == 1 means that the function in which this parameter will be used, 
            should return a single determiner or single noun or single present verb otherwise
            it will return a plural determiner or plural noun.
        verb_tense: a string that determines the verb conjugation,
            either "past", "present" or "future"..
    Return: A sentence that contains a determiner, a noun, a verb, and a prepositional phrase.
    """
    sentence = get_determiner(quantity).capitalize() + ' ' + get_noun(quantity) + ' ' + \
               get_verb(quantity, verb_tense) + ' ' + get_prepositional_phrase(quantity)
    return sentence

def make_sentence_with_two_prepositional_phrase(quantity, verb_tense):
    """Calls get_determiner, get_noun, get_prepositional_phrase, get_verb, and 
       get_prepositional_phrase functions and builds and return a sentence.

    Parameter
        quantity: an integer.
            If quantity == 1 means that the function in which this parameter will be used,
            should return a single determiner or single noun or single present verb otherwise 
            it will return a plural determiner or plural noun.
        verb_tense: a string that determines the verb conjugation,
            either "past", "present" or "future"..
    Return: A sentence that contains a determiner, a noun, a prepositional phrase, 
    a verb, and a prepositional phrase.
    """
    sentence = get_determiner(quantity).capitalize() + ' ' + get_noun(quantity) + ' ' + \
               get_prepositional_phrase(1) + ' ' + get_verb(quantity, verb_tense) + ' ' + get_prepositional_phrase(quantity)    
    return sentence

if __name__ == "__main__":
    main()