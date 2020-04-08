"""
Find if a string is palindrome
"""


def is_palindrome(s):
    flag = False

    i = 0
    j = len(s) - 1

    while i != j:
        if s[i] != s[j]:
            return flag

        i += 1
        j -= 1

    flag = True
    return flag


if __name__ == '__main__':
    print(is_palindrome('madam'))
    print(is_palindrome('gaurav'))
