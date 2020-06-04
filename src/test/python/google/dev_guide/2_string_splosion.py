def string_splosion(string):
    result = ''

    for i in range(1, len(string) + 1):
        result += string[0:i]

    return result


def test_string_splosion():
    assert string_splosion('Code') == 'CCoCodCode'
    assert string_splosion('ab') == 'aab'
    assert string_splosion('abc') == 'aababc'


"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

stringSplosion("Code") → "CCoCodCode"
stringSplosion("abc") → "aababc"
stringSplosion("ab") → "aab"
"""