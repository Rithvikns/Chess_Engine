# General Improvements:
- Consider using Enum for piece names to improve readability.

- Add type hints for move_piece parameters (piece: str).

- get_occupancy could use sum() instead of | for better clarity (sum([self.bitboards[p] for p in pieces])).

- Fixing these issues will make your code more robust and readable! 🚀