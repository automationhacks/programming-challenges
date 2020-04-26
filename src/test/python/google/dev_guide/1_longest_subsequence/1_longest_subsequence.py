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


if __name__ == '__main__':
    letter = "abppplee"
    words = ["able", "ale", "apple", "bale", "kangaroo"]
    result = longest_word_in_string(letter, words)
    assert result == "apple"
