# Chess
I Love the game chess and my focus on this project will be to implement a chess engine. 
I hope by building this project , I will understand the software engineering stuff and the game in detail.

## File Structure
```console
chess_engine/
│── src/
│   ├── __init__.py
│   ├── board.py          # Board representation & move generation
│   ├── move.py           # Move validation and application
│   ├── search.py         # Minimax, Alpha-Beta Pruning
│   ├── evaluation.py     # Position evaluation logic
│   ├── engine.py         # Main engine logic
│   ├── uci.py            # Universal Chess Interface (optional)
│── tests/                # Unit tests
│── Dockerfile            # Docker setup
│── pyproject.toml        # Poetry dependencies
│── README.md             # Project documentation
│── .gitignore            # Ignore unnecessary files
```

## Roadmap

- Setup & Environment
- Initialize Git repository.
- Board Representation
- Move Generation & Rules
- Search Algorithm
- Position Evaluation
- Playable Interface
- Optimization & Deployment

# Understanding Bitboards and Their Importance

## What are Bitboards?
A **bitboard** is a data structure that represents a game board using bits within an integer (or multiple integers). Instead of using an array or list to store board positions, a bitboard stores each position as a single bit in a binary number.

For example, in an 8×8 chessboard, we can use a **64-bit integer** where each bit represents a square on the board. A bit set to `1` might indicate the presence of a piece, while a bit set to `0` might indicate an empty square.

## Why Are Bitboards Needed?
Bitboards are widely used in board game engines, especially in games like **chess, checkers, and Go**, due to their efficiency in position representation and computation. Here’s why bitboards are superior to traditional lists or arrays:

### 1. **Memory Efficiency**
- A Python list of size 64 (for an 8×8 chessboard) contains references to objects, which adds significant memory overhead.
- A bitboard uses a single 64-bit integer, significantly reducing memory usage and improving **cache locality**.

### 2. **Speed Through Bitwise Operations**
- Instead of iterating through a list to check positions, bitwise operations allow near-instantaneous computations.
- **Examples of fast operations:**
  - Setting a bit (`board |= 1 << position`)
  - Clearing a bit (`board &= ~(1 << position)`)
  - Checking if a bit is set (`(board >> position) & 1`)

### 3. **CPU-Level Optimizations**
- Modern CPUs have optimized instructions for bitwise operations, allowing rapid evaluation of board states.
- **Population count (`popcount`)**: A CPU can count the number of set bits in a single instruction, which is useful for move generation in games like chess.

### 4. **Parallel Computation**
- Since bitwise operations act on all bits at once, multiple board positions can be processed **simultaneously**, avoiding slow loops.

## Example: Chessboard Representation with a Bitboard
Let’s consider a simple example where we store the positions of **pawns** on a chessboard using a bitboard.

### Step 1: Understanding the Bitboard Representation
A standard 8×8 chessboard is indexed as follows:

```
  8  56 57 58 59 60 61 62 63  
  7  48 49 50 51 52 53 54 55  
  6  40 41 42 43 44 45 46 47  
  5  32 33 34 35 36 37 38 39  
  4  24 25 26 27 28 29 30 31  
  3  16 17 18 19 20 21 22 23  
  2   8  9 10 11 12 13 14 15  
  1   0  1  2  3  4  5  6  7  
     a  b  c  d  e  f  g  h
```

Each square is represented by a bit in a **64-bit integer**. If a white pawn is at e2 (index `12`), the corresponding bit is set:

```
00000000 00000000 00000000 00000000 00000000 00000000 00010000 00000000
```

### Step 2: Moving a Pawn Forward
If a pawn moves forward, we can achieve this with a single bitwise **left shift** (`<<`), instead of modifying an array:

```
board = board << 8  # Moves all pawns forward one row
```

This operation is extremely fast compared to iterating through a list.

## Conclusion
Bitboards provide **compact, fast, and efficient** representation of board states, making them ideal for performance-critical applications like game engines. Through bitwise operations, computations that would normally take several loops in a list-based approach can be done **in a single CPU instruction**, leading to substantial performance improvements.

