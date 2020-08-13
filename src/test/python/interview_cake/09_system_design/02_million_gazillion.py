"""
I'm making a search engine called MillionGazillion™.

I wrote a crawler that visits web pages, stores a few keywords in a database,
and follows links to other web pages. I noticed that my crawler was wasting a
lot of time visiting the same pages over and over, so I made a set, visited,
where I'm storing URLs I've already visited. Now the crawler only visits a URL
if it hasn't already been visited.

Thing is, the crawler is running on my old desktop computer in my parents'
basement (where I totally don't live anymore) and it keeps running out of memory
because visited is getting so huge.

How can I trim down the amount of space taken up by visited?
"""

import unittest
from pprint import pprint

"""
If you've never heard of a trie, think of it this way:

Let's make visited a nested dictionary where each map has keys of just one
character. So we would store 'google.com' as
visited['g']['o']['o']['g']['l']['e']['.']['c']['o']['m']['*'] = True.

The '\*' at the end means 'this is the end of an entry'. Otherwise we wouldn't
know what parts of visited are real URLs and which parts are just prefixes. In
the example above, 'google.co' is a prefix that we might think is a visited URL
if we didn't have some way to mark 'this is the end of an entry.'

Now when we go to add 'google.com/maps' to visited, we only have to add the
characters '/maps', because the 'google.com' prefix is already there. Same with
'google.com/about/jobs'.

We can visualize this as a tree, where each character in a string corresponds to
a node.

A trie is a type of tree.

To check if a string is in the trie, we just descend from the root of the tree
to a leaf, checking for a node in the tree corresponding to each character in
the string.

How could we implement this structure? There are lots of ways! We could use
nested dictionaries, nodes and pointers, or some combination of the two.
Evaluating the pros and cons of different options and choosing one is a great
thing to do in a programming interview.

In our implementation, we chose to use nested dictionaries. To determine if a
given site has been visited, we just call add_word(), which adds a word to the
trie if it's not already there
"""


class Trie(object):
    def __init__(self):
        self.root_node = {}

    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False

        # work downwards in the Trie, adding nodes as needed
        # and keeping track of whether we add any nodes
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}

            current_node = current_node[char]

        # Explicitly mark the end of a word
        # Otherwise we might say a word is present if its
        # a prefix of a different longer work that was added earlier
        if "End of Word" not in current_node:
            is_new_word = True
            current_node["End of Word"] = {}

        return is_new_word


class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')

        pprint(trie.root_node, indent=2)


unittest.main(verbosity=2)