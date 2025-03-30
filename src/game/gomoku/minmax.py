from typing import List, Tuple

PLAYER_X = "X"
PLAYER_O = "O"  
EMPTY = "."
BOARD_SIZE = 20

def evaluate(board: List[List[str]]) -> int:
    if check_winner(board, PLAYER_X):
        return -1000 
    if check_winner(board, PLAYER_O):
        return 1000
    return heuristic_evaluation(board)  
def heuristic_evaluation(board: List[List[str]]) -> int:
    score = 0
    
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if j + 4 < BOARD_SIZE:
                score += evaluate_window([board[i][j+k] for k in range(5)])
                
            if i + 4 < BOARD_SIZE:
                score += evaluate_window([board[i+k][j] for k in range(5)])
                
            if i + 4 < BOARD_SIZE and j + 4 < BOARD_SIZE:
                score += evaluate_window([board[i+k][j+k] for k in range(5)])
                
            if i - 4 >= 0 and j + 4 < BOARD_SIZE:
                score += evaluate_window([board[i-k][j+k] for k in range(5)])
                
    return score

def evaluate_window(window: List[str]) -> int:
    if EMPTY not in window:
        return 0
        
    o_count = window.count(PLAYER_O)
    x_count = window.count(PLAYER_X)
    
    if x_count == 0 and o_count > 0:
        return o_count * 10
        
    if o_count == 0 and x_count > 0:
        return -x_count * 10
        
    return 0

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

def minimax(board: List[List[str]], depth: int, alpha: int, beta: int, maximizing: bool) -> Tuple[int, Tuple[int, int]]:
    if depth == 0 or check_winner(board, PLAYER_X) or check_winner(board, PLAYER_O):
        return evaluate(board), (-1, -1)
    
    empty_positions = get_empty_positions(board)
    
    if not empty_positions:
        return 0, (-1, -1)
        
    empty_positions.sort(key=lambda pos: distance_to_center(pos))
    
    if len(empty_positions) > 25:
        empty_positions = empty_positions[:25]
    
    best_move: Tuple[int, int] = empty_positions[0] if empty_positions else (-1, -1)
    
    if maximizing:  
        max_eval = float('-inf')
        for row, col in empty_positions:
            board[row][col] = PLAYER_O
            eval_score, _ = minimax(board, depth - 1, alpha, beta, False)
            board[row][col] = EMPTY  
            
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (row, col)
                
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
                
        return int(max_eval), best_move
        
    else:  
        min_eval = float('inf')
        for row, col in empty_positions:
            board[row][col] = PLAYER_X
            eval_score, _ = minimax(board, depth - 1, alpha, beta, True)
            board[row][col] = EMPTY  
            
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (row, col)
                
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
                
        return int(min_eval), best_move

def get_empty_positions(board: List[List[str]]) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE) if board[i][j] == EMPTY]

def distance_to_center(position: Tuple[int, int]) -> int:
    center = BOARD_SIZE // 2
    row, col = position
    return abs(row - center) + abs(col - center)
