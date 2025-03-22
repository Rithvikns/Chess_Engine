from dataclasses import dataclass , field

@dataclass
class board:
    def display(self):
        """Converts bitboards into a readable board format and prints it."""
        pass
    
    def set_piece(self, square: int, piece: str):
        """Updates the bitboard to add/remove a piece at a given square."""
        pass
    
    def move_piece(self, start: int, end: int):
        """Moves a piece from one square to another using bit manipulation."""
        pass
    
    def is_square_occupied(self, square: int) -> bool:
        """Checks if a square has any piece."""
        pass
    
    def get_occupancy(self, color: str):
        """Returns a combined bitboard of all pieces for a given color."""
        pass
    
    def to_fen(self) -> str:
        """Converts the bitboard position into FEN notation."""
        pass
    
    @classmethod
    def from_fen(cls, fen: str):
        """Loads a position from a FEN string into bitboards."""
        pass
    
    def position_hash(self) -> int:
        """Generates a unique hash for the current board state."""
        pass
