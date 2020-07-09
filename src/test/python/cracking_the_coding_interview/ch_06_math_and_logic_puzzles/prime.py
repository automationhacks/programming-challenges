import math


def is_prime(num):
    if num < 2:
        return False

    # Runtime is less than if we iterate till the no itself
    limit = int(math.sqrt(num))

    for i in range(2, limit):
        if num % i == 0:
            return False

    return True


def sieve_of_eratosthenes(num):
    """
    Generates prime nos until num
    """
    flags = [True] * (num + 1)
    flags[0], flags[1] = False, False
    length = len(flags)

    prime = 2

    while prime <= math.sqrt(num):
        i = prime * prime

        while i < len(flags):
            flags[i] = False
            i += prime

        next = prime + 1
        while next < length and not flags[next]:
            next += 1

        prime = next

    return flags


def test_is_prime():
    assert is_prime(19) is True
    assert is_prime(20) is False


def test_primes_print_using_sieve_of_eratosthenes():
    result = [index for index, flag in enumerate(sieve_of_eratosthenes(20)) if flag]
    assert result == [2, 3, 5, 7, 11, 13, 17, 19]
