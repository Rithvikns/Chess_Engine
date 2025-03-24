## Extra pass Statements

- pass is unnecessary in methods that already contain executable code.

- Remove pass from display, set_piece, move_piece, and get_occupancy.

- Fix Variable Name bitnoard_name

- In is_square_occupied, for bitnoard_name, bitboard in self.bitboards.items(): contains a typo.

- Change bitnoard_name to bitboard_name.

- Ensure FEN Uses Correct Characters

## When appending piece characters in to_fens, ensure they are correctly converted to FEN notation (though your current implementation looks mostly correct).

# General Improvements:
- Consider using Enum for piece names to improve readability.

- Add type hints for move_piece parameters (piece: str).

- get_occupancy could use sum() instead of | for better clarity (sum([self.bitboards[p] for p in pieces])).

- Fixing these issues will make your code more robust and readable! 🚀