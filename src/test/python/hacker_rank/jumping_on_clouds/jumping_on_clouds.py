# !/bin/python3

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    jumps = 0

    idx = 0
    while idx < n:
        try:
            cloud_at_next_jump = c[idx + 2]
            if cloud_at_next_jump == 1:
                idx += 1
            elif cloud_at_next_jump == 0:
                idx += 2
        except IndexError:
            break

        jumps += 1

    return jumps


def test_something():
    c = list(map(int, '0 0 0 0 1 0'.rstrip().split()))
    result = jumpingOnClouds(len(c), c)
    assert result == 3


def test_another_something():
    c = list(map(int, '0 0 0 1 0 0'.rstrip().split()))
    result = jumpingOnClouds(len(c), c)
    assert result == 3
