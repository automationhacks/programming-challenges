"""
    Print prime nos till a certain range

    Logic:
    1. Prime no is only divisible by 1 and itself
    2. To verify if modulus of a no by any no is 0 then it is not prime
"""


def is_prime(num):
    prime = False

    if num > 1:
        for i in range(2, num):
            # If remainder is 0 means divisible and hence not prime
            if (num % i) == 0:
                return prime
        # If entire loop is traversed without breaking means, no is prime
        prime = True

    return prime


def print_prime_nos():
    primes = []
    print('Enter the range till which prime nos is to be printed ')
    limit = int(input())

    for nos in range(2, limit):
        if is_prime(nos):
            primes.append(nos)

    print('All primes till range {}'.format(primes))


if __name__ == '__main__':
    print_prime_nos()
