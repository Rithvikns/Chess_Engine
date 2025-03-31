from dataclasses import dataclass
import board

print(board.Board.bitboards)
@dataclass
class Engine:
    depth : int = 3
    color : str = 'white'

    def generate_legal_moves(self):
        """Generates all legal moves for the current position."""
        if board.Board.side_to_move == 'w':
            self.color = 'white'
        else:
            self.color = 'black'
        own_pieces = board.Board.get_occupancy(self.color)
        enemy_pieces = board.Board.get_occupancy('black' if self.color == 'white' else 'white')
        all_pieces = own_pieces | enemy_pieces
        if board.Board.enpassant != '-':
            ep_square = board.Board.get_enpassant_square()
        
        # pawn moves

        pawns = board.Board.bitboards('P') if self.color == 'white' else 'black'
        push_dir = 8 if self.color == 'white' else -8
        promotion_rank = (pawns & 0xFF00000000000000) if self.color == 'white' else (pawns & 0x00000000000000FF)

        for pawn in pawns:
            pass

    def is_move_legal(self, board, move: tuple) -> bool:
        """Checks if a move is legal."""
        pass

    def evaluate_position(self, board) -> int:
        """Assigns a numerical value to a given position based on evaluation metrics."""
        pass

    def minimax(self, board, depth: int, maximizing: bool) -> int:
        """Implements the Minimax algorithm for decision-making."""
        pass

    def alpha_beta(self, board, depth: int, alpha: int, beta: int, maximizing: bool) -> int:
        """Optimized Minimax using Alpha-Beta pruning."""
        pass

    def quiescence_search(self, board, alpha: int, beta: int) -> int:
        """Handles quiet positions to avoid horizon effects."""
        pass

    def select_best_move(self, board) -> tuple:
        """Finds the best move for the current position."""
        pass

    def is_game_over(self, board) -> bool:
        """Checks if the game has ended (checkmate, stalemate, etc.)."""
        pass

    def perft(self, board, depth: int) -> int:
        """Performs a perft test to count legal move positions up to a given depth."""
        pass
