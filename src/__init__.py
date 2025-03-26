# Import essential classes and functions to make them accessible at the package level
from .board import Board

# Define a default starting position in FEN notation
DEFAULT_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Expose key components of the package
__all__ = ["Board", "DEFAULT_FEN"]