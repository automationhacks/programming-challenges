def test_can_balance_valid():
    assert can_balance([1, 1, 1, 2, 1]) is True


def test_can_balance_invalid():
    assert can_balance([2, 1, 1, 2, 1]) is False


def test_can_balance_valid_with_two_numbers():
    assert can_balance([10, 10]) is True


def can_balance(arr):
    found = False
    pos = 0
    end = len(arr)

    while pos < end and not found:
        left = arr[0:pos]
        right = arr[pos:end]

        if sum(left) == sum(right):
            found = True

        pos += 1

    return found
