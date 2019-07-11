class Position:
    def __init__(self, x, y):
        check_pos(x, y)
        self._x = x
        self._y = y


def check_pos(x, y):
    if x not in range(1, 9):
        raise ValueError(str(x) + " must be in (1 - 8) range")
    if y not in range(1, 9):
        raise ValueError(str(y) + " must be in (1 - 8) range")

