"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/goat-latin/
Topic: String

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and
uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

    If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
    For example, the word 'apple' becomes 'applema'.

    If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
    For example, the word "goat" becomes "oatgma".

    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
    For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin.

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


Notes:

    S contains only uppercase, lowercase and spaces. Exactly one space between each word.
    1 <= S.length <= 150.
"""


class Solution:
    def toGoatLatin(self, normal_string: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        suffix_char = 'a'
        result = []

        splitted = normal_string.split(' ')

        for index, word in enumerate(splitted):
            first_char = word[0]
            suffix_string = suffix_char * (index + 1)

            if first_char in vowels:
                word_to_append = f'{word}ma{suffix_string}'
                result.append(word_to_append)
            else:
                word_to_append = f'{word[1:]}{word[0]}ma{suffix_string}'
                result.append(word_to_append)

        return ' '.join(result)


def test_short_string_to_goat_latin():
    assert Solution().toGoatLatin('I speak Goat Latin') == 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'


def test_long_string_to_goat_latin():
    assert Solution().toGoatLatin(
        'The quick brown fox jumped over the lazy dog') == 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa'
