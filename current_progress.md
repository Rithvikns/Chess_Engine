# Corrections & Fixes
Fix from_fen Method Implementation

The line cls.bitboards = dict.fromkeys(cls.bitboards.keys(),0) incorrectly tries to modify a class variable rather than an instance variable. Instead, create a new bitboards dictionary inside the method.

The bit shifting (1 << (i*8+j)) is incorrect. It should correctly account for rank and file.

position_hash Should Be Inside the Class

The method position_hash(self) is currently defined outside the class. It should be included inside Board with self referring to the instance.

# Improvements
Enforce Type Annotations Consistently

Some methods, such as move_piece, set_piece, and get_occupancy, lack explicit return types. Add them for better clarity and debugging.

# Improve display Method

The board representation could be enhanced by using chessboard-like formatting rather than printing lists.

# Optimize Bitwise Operations

Instead of iterating over all 64 squares in is_square_occupied, you could use any((bitboard >> square) & 1 for bitboard in self.bitboards.values()).

# Refine to_fens Method

Rename it to to_fen for consistency with from_fen.

Ensure castling and en passant are properly formatted.