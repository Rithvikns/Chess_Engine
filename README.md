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
- 1. Setup & Environment
Install Poetry and Docker.
Set up pyproject.toml with dependencies.
Initialize Git repository.
- 2. Board Representation
Choose 0x88 or Bitboard representation.
Implement move generation and validation.
- 3. Move Generation & Rules
Implement all piece moves (pawns, knights, etc.).
Add castling, en passant, and promotion.
- 4. Search Algorithm
Implement Minimax.
Optimize with Alpha-Beta Pruning.
- 5. Position Evaluation
Design a scoring system for piece values, mobility, etc.
- 6. Playable Interface
Add UCI (Universal Chess Interface) for external GUIs.
Create a simple CLI.
- 7. Optimization & Deployment
Profile performance.
Optimize data structures.
Dockerize the project.
