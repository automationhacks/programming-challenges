def print_fibonacci(limit):
    """
    Logic:
        1. Store 0 and 1 as a and b and store in output list
        2. Add a var c to store sum of a and b i.e. new no
        3. store value of 2nd no in first i.e. lose value of first no
        4. store value of 3rd in 2nd
    :param limit: how many fibonacci nos are required
    :return: output list with fibonacci nos
    """
    a = 0
    b = 1

    output = [a, b]

    while len(output) < limit:
        c = a + b
        a = b
        b = c

        output.append(c)
    return output


def recurse_fibonacci(pos1, pos2, limit):
    """
    1. pass last 2 nos, pos1, pos2
    2. sum pos1 and pos2 as pos3 and print
    3. if pos3 < limit of nos return
    2. exchange pos1 with pos2
    3. exchange pos2 with pos3
    4. again recurse
    :return:
    """

    pos3 = pos1 + pos2

    if pos3 >= limit:
        return

    pos1 = pos2
    pos2 = pos3

    return str(pos3) + ' ' + str(recurse_fibonacci(pos1, pos2, limit))


def recurse_fibonacci_v2(n):
    """
    I dont get this, need to explain how this works
    in recursive terminology
    :param n:
    :return:
    """
    if n <= 1:
        return n
    else:
        return recurse_fibonacci_v2(n - 1) + recurse_fibonacci_v2(n - 2)


def recurse_fibo_wrapper(limit):
    for i in range(limit):
        print(recurse_fibonacci_v2(i))


if __name__ == '__main__':
    print(print_fibonacci(20))

    pos1, pos2 = 0, 1
    output = recurse_fibonacci(pos1, pos2, 4181)
    print(str(pos1) + ' ' + str(pos2) + ' ' + output)

    limit = int(input('Enter limit '))
    recurse_fibo_wrapper(limit)
