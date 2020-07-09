def triple_step(steps):
    if steps < 0:
        return 0
    if steps == 0:
        return 1
    if steps == 1:
        return 1

    return triple_step(steps - 1) + triple_step(steps - 2) + triple_step(steps - 3)


def triple_steps_recursive(steps, memo):
    if steps < 0:
        return 0
    memo[0] = 1

    if steps >= 1:
        memo[1] = 1

    if steps >= 2:
        memo[2] = memo[1] + memo[0]

    if steps > 2:
        for i in range(3, steps + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    return memo[steps]


def triple_step_with_memo(steps):
    memo = [-1] * (steps + 1)
    return triple_steps_recursive(steps, memo)


def test_triple_step():
    print()
    print(triple_step(6))
    print(triple_step_with_memo(6))
