import unittest

""" 
Problem statement

You want to build a word cloud, an infographic where the size of a word corresponds to 
how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word 
cloud data in a dictionary ↴ , where the keys are words and the values are the number 
of times the words occurred.

Think about capitalized words. For example, look at these sentences:

  'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'

What do we want to do with "After", "Dana", and "add"? In this example, your final 
dictionary should include one "Add" or "add" with a value of 2. Make reasonable 
(not necessarily perfect) decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.

You could make a reasonable argument to use regex in your solution. We won't, 
mainly because performance is difficult to measure and can get pretty bad.
"""

# O(n)
class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word
        self.words_to_counts = {}
        words = self.split_words(input_string)
        self.count_words(words)


    def split_words(self, input_string):
        acceptable_chars = set("'")
        words = []

        temp = []
        for index, ch in enumerate(input_string):

            # if we have reached the end
            # then we add the word which is under process
            if index == len(input_string) - 1:
                if ch.isalpha():
                    temp.append(ch)
                words.append(''.join(temp))
                break

            # Keep on appending chars till they are valid
            if ch.isalpha() or ch in acceptable_chars:
                temp.append(ch)
            # If non alphabet or non acceptable chars are encountered
            # then add the word in process to list
            else:
                if temp:
                    words.append(''.join(temp))
                    temp = []
        return words


    def count_words(self, words):
        for word in words:
            if word in self.words_to_counts:
                self.words_to_counts[word] += 1
            # Handle case wherein same key with first letter in
            # capital is present in the word cloud
            elif word.capitalize() in self.words_to_counts:
                to_remove = word.capitalize()
                count = self.words_to_counts[to_remove]
                self.words_to_counts.pop(to_remove)
                self.words_to_counts[word.lower()] = count + 1
            else:
                self.words_to_counts[word] = 1


# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille': 1,'feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts
        print(actual)

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)

