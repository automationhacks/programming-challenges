"""
Input: 'hello my friend, can you caps the first letters?'
Output: 'Hello My Friend, Can You Caps The First Letters?'
"""


def capsify(strng):
    output = ''

    if len(strng) == 1:
        if strng.islower():
            return strng.upper()
    else:
        i = 0
        while i < len(strng):
            if i == 0:
                output += strng[i].upper()
            elif strng[i] == ' ':
                output += ' ' + strng[i + 1].upper()
                i += 1
            else:
                output += strng[i]

            i += 1
        return output


if __name__ == '__main__':
    print(capsify('hello my friend, can you caps the first letters?'))
