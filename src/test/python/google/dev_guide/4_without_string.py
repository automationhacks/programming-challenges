"""
Given two strings, base and remove, return a version of the base string where all instances of the remove string have
been removed (not case sensitive). You may assume that the remove string is length 1 or more.
Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".

withoutString("Hello there", "llo") → "He there"
withoutString("Hello there", "e") → "Hllo thr"
withoutString("Hello there", "x") → "Hello there"
"""


def without_string(base, to_remove):
    result = ''

    # Learning: If you are going to jump in the outer loop (do not use i in range())
    # Prefer a while loop where you have control over the index
    i = 0
    while i < len(base):
        curr_char = base[i]

        if curr_char.lower() != to_remove[0].lower():
            result += curr_char
            i += 1
        else:
            no_match_found = False
            start = 0
            end = len(to_remove)
            temp = ''

            while start < end and not no_match_found:
                char_from_base = base[i + start]
                temp += char_from_base
                char_to_remove = to_remove[start]

                if char_from_base.lower() != char_to_remove.lower():
                    no_match_found = True

                start += 1

            if no_match_found:
                result += temp

            i += start

    return result


def without_string_optimized(base, to_remove):
    rem_len = len(to_remove)

    while True:
        try:
            rem_idx = base.lower().index(to_remove.lower())
        except ValueError:
            break
        base = base[0:rem_idx] + base[rem_idx + rem_len:]
    return base


def test_char_to_remove_in_base():
    assert without_string_optimized("Hello there", "llo") == "He there"
    assert without_string_optimized("Hello there", "e") == "Hllo thr"


def test_base_has_upper_case():
    assert without_string_optimized("HeLLo there", "llo") == "He there"


def test_to_remove_has_upper_case():
    assert without_string_optimized("Hello there", "LLo") == "He there"


def test_char_to_remove_not_in_string():
    assert without_string_optimized("Hello there", "x") == "Hello there"
