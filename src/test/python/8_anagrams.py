"""
Find if two strings are anagrams
"""


def are_anagrams(string1, string2):
    is_anagram = False
    letters_count_string1 = {}
    letters_count_string2 = {}

    if len(string1) != len(string2):
        return is_anagram
    else:
        i = 0
        limit = len(string1)

        while i < limit:

            if string1[i] in letters_count_string1.keys():
                letters_count_string1[string1[i]] += 1
            else:
                letters_count_string1[string1[i]] = 0

            if string2[i] in letters_count_string2.keys():
                letters_count_string2[string2[i]] += 1
            else:
                letters_count_string2[string2[i]] = 0

            i += 1

        if letters_count_string1 == letters_count_string2:
            is_anagram = True

        return is_anagram


if __name__ == '__main__':
    print(are_anagrams('complex', 'celmopx'))
