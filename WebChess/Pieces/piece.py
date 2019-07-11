import abc


class Piece:
    def __init__(self, pos, color):
        self._pos = pos
        self._color = color

    """
    Function returns all valid moves based solely
    on the piece's state. State of the chessboard is not
    taken into consideration.
    """

    @abc.abstractmethod
    def get_valid_moves(self):
        pass

    """
    Changes position of the piece.
    """

    def move(self, pos):
        self._pos = pos
