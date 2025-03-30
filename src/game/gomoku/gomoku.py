from minmax import minimax
from typing import List, Tuple

BOARD_SIZE = 20
EMPTY = "."
PLAYER_X = "X"
PLAYER_O = "O"

def create_board() -> List[List[str]]:
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] 

def print_board(board: List[List[str]]) -> None:
    for row in board:
        print(" ".join(row))

def check_winner(board: List[List[str]], player: str) -> bool:
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if j + 4 < BOARD_SIZE and all(board[i][j+k] == player for k in range(5)):
                return True
            if i + 4 < BOARD_SIZE and all(board[i+k][j] == player for k in range(5)):
                return True
            if i + 4 < BOARD_SIZE and j + 4 < BOARD_SIZE and all(board[i+k][j+k] == player for k in range(5)):
                return True
            if i - 4 >= 0 and j + 4 < BOARD_SIZE and all(board[i-k][j+k] == player for k in range(5)):
                return True
    return False

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

def ai_move(board: List[List[str]]) -> Tuple[int, int]:
    _, best_move = minimax(board, 3, -10**9, 10**9, True) 
    return best_move

def main() -> None:
    board = create_board()
    print_board(board)
    
    while True:
        row, col = player_move(board)
        board[row][col] = PLAYER_X
        print_board(board)
        
        if check_winner(board, PLAYER_X):
            print("Player X wins!")
            break
            
        if not get_empty_positions(board):
            print("It's a draw!")
            break
            
        print("AI is thinking...")
        row, col = ai_move(board)
        print(f"AI plays at: {row}, {col}")
        board[row][col] = PLAYER_O
        print_board(board)
        
        if check_winner(board, PLAYER_O):
            print("Player O wins!")
            break
            
        if not get_empty_positions(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
