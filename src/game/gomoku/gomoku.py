
import numpy as np

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_win(board, player):
    for i in range(5):
        if all(board[i, j] == player for j in range(5)) or all(board[j, i] == player for j in range(5)):
            return True
    if all(board[i, i] == player for i in range(5)) or all(board[i, 4 - i] == player for i in range(5)):
        return True
    return False

def gomoku():
    board = np.full((5, 5), '.', dtype=str)
    players = ['X', 'O']
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-4): ").split())
            if board[row, col] != '.':
                print("Cell occupied! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter numbers between 0 and 4.")
            continue
        
        board[row, col] = player
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if '.' not in board:
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1

gomoku()
