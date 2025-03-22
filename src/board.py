from dataclasses import dataclass , field
bitboard = {
    'white_pawns'   : 0b00000000_00000000_00000000_0000000_00000000_00000000_11111111_00000000,
    'white_knights' : 0b00000000_00000000_00000000_0000000_00000000_00000000_00000000_01000010,
    'white_rooks'   : 0b00000000_00000000_00000000_0000000_00000000_00000000_00000000_10000001,
    'white_bishops' : 0b00000000_00000000_00000000_0000000_00000000_00000000_00000000_00100100,
    'white_queen'   : 0b00000000_00000000_00000000_0000000_00000000_00000000_00000000_00010000,
    'white_king'    : 0b00000000_00000000_00000000_0000000_00000000_00000000_00000000_00001000,
    'black_pawns'   : 0b00000000_11111111_00000000_0000000_00000000_00000000_00000000_00000000,
    'black_knights' : 0b01000010_00000000_00000000_0000000_00000000_00000000_00000000_00000000,
    'black_rooks'   : 0b10000001_00000000_00000000_0000000_00000000_00000000_00000000_00000000,
    'black_bishops' : 0b00100100_00000000_00000000_0000000_00000000_00000000_00000000_00000000,
    'black_queen'   : 0b00010000_00000000_00000000_0000000_00000000_00000000_00000000_00000000,
    'black_king'    : 0b00001000_00000000_00000000_0000000_00000000_00000000_00000000_00000000
  
}

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
