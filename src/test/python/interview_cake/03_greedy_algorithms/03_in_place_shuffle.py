import random

"""
Problem statement:

Write a function for doing an in-place shuffle of a list.
The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in 
each spot in the final list.
Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
"""

"""
Solution:
O(n) time and O(1) space

We choose a random item to move to the first index, then we choose a random other item to move to the second index, etc.
 We "place" an item in an index by swapping it with the item currently at that index.
Crucially, once an item is placed at an index it can't be moved. So for the first index, we choose from nnn items, for 
the second index we choose from n−1n-1n−1 items, etc. 
This is a semi-famous algorithm known as the Fisher-Yates shuffle (sometimes called the Knuth shuffle). 
"""


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    for current_index, num in enumerate(the_list):
        random_index = get_random(0, len(the_list) - 1)

        if random_index != current_index:
            temp = the_list[random_index]
            the_list[random_index] = num
            the_list[current_index] = temp

    # Shuffle the input in place

    pass


if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]

    for i in range(0, 20):
        print('Sample list:', sample_list)

        print('Shuffling sample list...')
        shuffle(sample_list)
        print(sample_list)
