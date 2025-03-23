# Forsyth-Edwards Notation (FEN) in Chess Engines 🏁

FEN is a standard notation for representing a chess position as a single line of text. It is widely used in chess engines to store and share board states.

## FEN Format

A FEN string consists of six fields, separated by spaces:

- Piece Placement – The board position from rank 8 to rank 1, using piece symbols (KQRBNP for white, kqrbnp for black) and numbers to indicate empty squares.

- Active Color – Whose turn it is (w for White, b for Black).

- Castling Rights – Available castling moves (KQkq for White/Black kingside/queenside castling, or - if none).

- En Passant Target Square – If a pawn moves two squares forward, this shows the en passant target (e.g., e3), otherwise -.

- Halfmove Clock – Counts moves since the last pawn move or capture (for the 50-move rule).

- Fullmove Number – Starts at 1 and increments after Black’s move.

## Example FEN String

The standard starting position in chess:
```console

rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```

### Breakdown:

- rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR → The board setup.

- w → White to move.

- KQkq → Both sides can castle kingside (Kk) and queenside (Qq).

- '-' → No en passant target square.

- 0 → No halfmoves made yet.

- 1 → First full move.

## How This Is Used in a Chess Engine

- The engine generates a FEN string to store the board state.

- It can load a position from a FEN string for analysis.

- It helps in game state tracking and debugging.

# FEN in Action
You can test FEN strings using online tools like Lichess FEN Editor.

- 📌 Implementing FEN parsing and generation is crucial for a chess engine. This ensures proper board representation and game state handling!

