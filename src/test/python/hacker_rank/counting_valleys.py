#!/bin/python3
from unittest import TestCase


def counting_valleys(n, s):
    valleys = 0
    path = 0

    for index, step in enumerate(s):
        if step == 'U':
            path += 1
        elif step == 'D':
            path -= 1
        else:
            raise NameError('Invalid input')

        valleys = is_out_of_valley(path, step, valleys)

    return valleys


def is_out_of_valley(path, step, valleys):
    if path == 0 and step == 'U':
        valleys += 1
    return valleys


class CountingTest(TestCase):

    def test_counting_valleys(self):
        input = 'DDUUDDUDUUUD'
        result = counting_valleys(len(input), input)
        self.assertEquals(result, 2)
