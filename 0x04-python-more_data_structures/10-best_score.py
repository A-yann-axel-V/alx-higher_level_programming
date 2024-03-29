#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Return the key with the biggest integer value.
    If no score found, return None.
    """
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
