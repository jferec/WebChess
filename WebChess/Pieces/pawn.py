from WebChess.Pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, pos, color):
        super().__init__(pos, color)
        self._has_moved = False

    def get_valid_moves(self):
        pass

    def move(self, pos):
        pass
