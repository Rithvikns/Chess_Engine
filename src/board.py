from dataclasses import dataclass , field
import random

@dataclass
class Board:
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

    zobrist_table : dict = field(init=False)
    def __post_init__(self):
        self.zobrist_table = {
            "piece": {square: random.getrandbits(64) for square in range(64) for piece in self.bitboards.keys()},
            "castling": [random.getrandbits(64) for _ in range(4)],  # 4 castling rights
            "en_passant": {file: random.getrandbits(64) for file in range(8)},  # 8 possible en passant files
            "side_to_move": random.getrandbits(64)  # Single value for White/Black
            }
    

    side_to_move = 'w'
    castling_rights = "KQkq"
    enpassent = '-'
    half_move = 0
    full_move = 1


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
        
    
    def set_piece(self, square: int, piece: str):
        """Updates the bitboard to add/remove a piece at a given square."""
        self.bitboards[piece] = self.bitboards[piece] | (1 << square)
        
    
    def move_piece(self,piece, start: int, end: int):
        """Moves a piece from one square to another using bit manipulation."""
        self.bitboards[piece] = self.bitboards[piece] & (~(1 << start))
        self.bitboards[piece] = self.bitboards[piece] | (1 << end)
        
    
    def is_square_occupied(self, square: int) -> bool:
        """Checks if a square has any piece."""
        for bitboard in self.bitboards.values():
            if (bitboard >> square ) & 1:
                return True
        
        return False
    
    def get_occupancy(self, color: str):
        """Returns a combined bitboard of all pieces for a given color."""
        if  color ==  "White":
            return(self.bitboards['P'] | self.bitboards['N'] | self.bitboards['R'] | self.bitboards['B'] | self.bitboards['Q'] | self.bitboards['K']) 
        else:
            return(self.bitboards['p'] | self.bitboards['n'] | self.bitboards['r'] | self.bitboards['b'] | self.bitboards['q'] | self.bitboards['k']) 
            
    
    def to_fens(self, side_to_move, castling, enpassant, half_move, full_move) -> str:
        """Converts the bitboard position into FEN notation."""
        output = ""
        chess_board = [[0] * 8 for _ in range(8)]

        # Place pieces on board
        for board_name, bitboard in self.bitboards.items():
            for i in range(64):
                if (bitboard >> i) & 1:
                    row = 7 - (i // 8)
                    col = i % 8
                    chess_board[row][col] = board_name

        # Convert board to FEN
        fen_rows = []
        for row in chess_board:
            fen_row = ""
            empty_count = 0
            for col in row:
                if col == 0:
                    empty_count += 1
                else:
                    if empty_count > 0:
                        fen_row += str(empty_count)
                        empty_count = 0
                    fen_row += str(col)  # Ensure col represents correct FEN characters
            if empty_count > 0:
                fen_row += str(empty_count)  # Add trailing empty squares if any
            fen_rows.append(fen_row)

        output = "/".join(fen_rows)  # Join rows with "/"
        output += f" {side_to_move} {castling} {enpassant} {half_move} {full_move}"
        
        return output
    
    @classmethod
    def from_fen(cls, fen: str):
        """Loads a position from a FEN string into bitboards."""
        cls.bitboards = dict.fromkeys(cls.bitboards.keys(),0)
        fen_list = fen.split(" ")
        pos_list = fen_list[0].split("/")
        for i in range(len(pos_list)):
            pos = pos_list[i]
            for j in len(pos):
                if pos[j].isnumeric():
                    continue
                else:
                    cls.bitboards[pos[j]] |= (1 << (i*8+j))
        cls.side_to_move = fen_list[1]
        cls.castling_rights = fen_list[2]
        cls.enpassent = fen_list[3]
        cls.half_move = fen_list[4]
        cls.full_move = fen_list[5]
    
    def position_hash(self) -> int:
        """Generates a unique hash for the current board state."""
        hash_value = 0
        for piece,bitboard in self.bitboards.items():
            for i in range(64):
                if (bitboard >> i) & 1 :
                    hash_value ^= self.zobrist_table[piece][i]
        
