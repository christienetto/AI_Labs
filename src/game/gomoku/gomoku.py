from typing import List, Tuple, Set
from ai import minimax, update_candidate_moves, check_winner_last_move

BOARD_SIZE = 20
EMPTY = "."
PLAYER_X = "X"
PLAYER_O = "O"

def create_board() -> List[List[str]]:
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board: List[List[str]]) -> None:
    for row in board:
        print(" ".join(row))

def get_empty_positions(board: List[List[str]]) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if board[i][j] == EMPTY]

def player_move(board: List[List[str]]) -> Tuple[int, int]:
    while True:
        try:
            move = input(f"Player {PLAYER_X}, enter row and column (0-19): ").split()
            row, col = int(move[0]), int(move[1])
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == EMPTY:
                return row, col
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter two integers between 0 and 19.")

def ai_move(board: List[List[str]], last_move: Tuple[int, int], candidate_moves: Set[Tuple[int, int]]) -> Tuple[int, int]:
    _, best_move = minimax(board, 3, -10**9, 10**9, True, candidate_moves, last_move)
    return best_move

def main() -> None:
    board = create_board()
    print_board(board)
    last_move = (BOARD_SIZE // 2, BOARD_SIZE // 2)
    candidate_moves = update_candidate_moves(set(), last_move, board)

    while True:
        row, col = player_move(board)
        board[row][col] = PLAYER_X
        print_board(board)
        last_move = (row, col)
        candidate_moves = update_candidate_moves(candidate_moves, last_move, board)

        if check_winner_last_move(board, last_move):
            print("Player X wins!")
            break

        if not get_empty_positions(board):
            print("It's a draw!")
            break

        print("AI is thinking...")
        row, col = ai_move(board, last_move, candidate_moves)
        print(f"AI plays at: {row}, {col}")
        board[row][col] = PLAYER_O
        print_board(board)
        last_move = (row, col)
        candidate_moves = update_candidate_moves(candidate_moves, last_move, board)

        if check_winner_last_move(board, last_move):
            print("Player O wins!")
            break

        if not get_empty_positions(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()

