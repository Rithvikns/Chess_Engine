
# Chessboard Representation using Bitboards

T# Bitboard Representation of a Chess Board

## How to Store the Board in Bitboard Format?

Instead of using a single 8x8 array, we represent the chessboard using 12 separate bitboards, one for each piece type and color.

### Bitboard Indexing

| Index | Bitboard Name    | Description             |
|--------|----------------|-------------------------|
| 0      | white_pawns    | White pawns (P)        |
| 1      | white_knights  | White knights (N)      |
| 2      | white_bishops  | White bishops (B)      |
| 3      | white_rooks    | White rooks (R)        |
| 4      | white_queens   | White queens (Q)       |
| 5      | white_kings    | White kings (K)        |
| 6      | black_pawns    | Black pawns (p)        |
| 7      | black_knights  | Black knights (n)      |
| 8      | black_bishops  | Black bishops (b)      |
| 9      | black_rooks    | Black rooks (r)        |
| 10     | black_queens   | Black queens (q)       |
| 11     | black_kings    | Black kings (k)        |

### Explanation
Each bitboard is a 64-bit integer, where each bit corresponds to a square on the chessboard. If a bit is set to `1`, it means a piece of that type is present on that square; otherwise, it's `0`.

This representation allows for efficient bitwise operations, making move generation and position evaluation much faster than traditional array-based methods.
