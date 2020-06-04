from collections import defaultdict


def longest_word_in_string(letters, words):
    letters_position = defaultdict(list)

    # collect indices for each letter as a list
    # complexity = O(n) n = no of letters
    for index, letter in enumerate(letters):
        letters_position[letter].append(index)

    # Iterate thru words in desc order of length
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0

        for letter in word:
            # Bail out if letter is not present in letters
            if letter not in letters_position:
                break

            possible_positions = [p for p in letters_position[letter] if p >= pos]
            if not possible_positions:
                break

            pos = possible_positions[0] + 1
        else:
            # We did not break out of the loop and hence all letters have valid position
            return word


def test_longest_word_in_subsequence():
    letter = "abppplee"
    words = ["able", "ale", "apple", "bale", "kangaroo"]
    assert longest_word_in_string(letter, words) == 'apple'


"""
# The Challenge

Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
"""
