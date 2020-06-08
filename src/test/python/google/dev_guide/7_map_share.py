"""
Modify and return the given map as follows:
if the key "a" has a value, set the key "b" to have that same value.
In all cases remove the key "c", leaving the rest of the map unchanged.

mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
mapShare({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
mapShare({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}
"""


def map_share(input_map):
    if 'a' in input_map.keys():
        input_map['b'] = input_map['a']

    if 'c' in input_map.keys():
        input_map.pop('c')

    return input_map


def test_map_share():
    assert map_share({"a": "aaa", "b": "bbb", "c": "ccc"}) == {"a": "aaa", "b": "aaa"}
    assert map_share({"b": "xyz", "c": "ccc"}) == {"b": "xyz"}
    assert map_share({"a": "aaa", "c": "meh", "d": "hi"}) == {"a": "aaa", "b": "aaa", "d": "hi"}
