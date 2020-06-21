"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
"""

from collections import Counter


# O(n)
def palindrome_permutation(string):
    alpha_chars = [ch for ch in string.lower() if ch.isalpha()]
    mapping = Counter(alpha_chars)
    number_of_odd = sum([1 for count in mapping.values() if count % 2])
    return number_of_odd <= 1


def test_palindrome_permutation():
    assert palindrome_permutation('Tact Coa') is True
