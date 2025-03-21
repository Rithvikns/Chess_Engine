from dataclasses import dataclass , field

@dataclass
class board:
    bitboards : dict = field(default_factory=lambda: {
    'P' : 0b00000000_00000000_00000000_00000000_00000000_00000000_11111111_00000000,
    'N' : 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_01000010,
    'R' : 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_10000001,
    'B' : 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00100100,
    'Q' : 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00010000,
    'K' : 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00001000,
    'p' : 0b00000000_11111111_00000000_00000000_00000000_00000000_00000000_00000000,
    'n' : 0b01000010_00000000_00000000_00000000_00000000_00000000_00000000_00000000,
    'r' : 0b10000001_00000000_00000000_00000000_00000000_00000000_00000000_00000000,
    'b' : 0b00100100_00000000_00000000_00000000_00000000_00000000_00000000_00000000,
    'q' : 0b00010000_00000000_00000000_00000000_00000000_00000000_00000000_00000000,
    'k' : 0b00001000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
  
    })

    def display(self):
        """Converts bitboards into a readable board format and prints it."""
        chess_board = [[0]*8 for _ in range(8)]
        for board_name , bitboard in self.bitboards.items():
            for i in range(64):
                if ((bitboard >> i) & 1):
                    row = 7 - (i//8)
                    col = i % 8
                    chess_board[row][col] = board_name
        for row in chess_board:
            print(row)
        pass
    
    def set_piece(self, square: int, piece: str):
        """Updates the bitboard to add/remove a piece at a given square."""
        self.bitboards[piece] = self.bitboards[piece] | (1 << square)
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
