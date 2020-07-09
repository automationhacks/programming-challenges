def fib(limit):
    a = 0
    b = 1

    fib_sequence = [a, b]

    while len(fib_sequence) < limit:
        c = a + b
        a = b
        b = c

        fib_sequence.append(c)
    return fib_sequence


def fib_recurse(num):
    if num <= 1:
        return num
    else:
        return fib_recurse(num - 1) + fib_recurse(num - 2)


# Uses memoization to cache intermediate results
# Runtime approx 1.6 ^ n since the right side tree is shorter
def fib_memo(num, memo):
    if num == 0 or num == 1:
        return num

    if memo[num] == 0:
        memo[num] = fib_memo(num - 1, memo) + fib_memo(num - 2, memo)

    return memo[num]


if __name__ == '__main__':
    nth = 20
    result = fib(nth - 1)
    print(sum(result), len(result))
    print(fib_recurse(nth))
    print(fib_memo(nth, [0] * (nth + 1)))
