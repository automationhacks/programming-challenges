OBSTACLE = 'O'
TRIED = '.'


class RobotInMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.exit = (self.rows - 1, self.cols - 1)
        self.paths = []

    def search_from(self, row, col):
        if row == self.rows or col == self.cols:
            return False

        if self.matrix[row][col] == OBSTACLE:
            return False

        if self.matrix[row][col] == TRIED:
            return False

        try:
            self.matrix[row][col] = TRIED
        except IndexError:
            return False

        if self.is_exit(row, col):
            self.paths.append((row, col))
            print(f'({row},{col})')
            return True

        found = self.search_from(row + 1, col) or self.search_from(row, col + 1)
        if found:
            print(f'({row},{col})')
        return found

    def is_exit(self, row, col):
        if row == self.exit[0] and col == self.exit[1]:
            return True


def test_robot_in_matrix():
    initial_matrix = [
        [0, 0, 0],
        [0, 'O', 0],
        [0, 0, 0]
    ]

    matrix = RobotInMatrix(initial_matrix)
    is_path = matrix.search_from(0, 0)

    print()
    print(f'is_path: {is_path}')
    if is_path:
        pass
