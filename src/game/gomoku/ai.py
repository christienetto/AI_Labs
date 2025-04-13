from typing import List, Tuple, Set

BOARD_SIZE = 20
EMPTY = "."
PLAYER_X = "X"
PLAYER_O = "O"

def minimax(board: List[List[str]], depth: int, alpha: int, beta: int, maximizing: bool,
            candidate_moves: Set[Tuple[int, int]], last_move: Tuple[int, int]) -> Tuple[int, Tuple[int, int]]:
    if depth == 0 or check_winner_last_move(board, last_move):
        return evaluate(board), (-1, -1)

    sorted_moves = sorted(candidate_moves, key=lambda move: distance_to(last_move, move))
    best_move = next(iter(sorted_moves), (-1, -1))

    if maximizing:
        max_eval = float('-inf')
        for move in sorted_moves:
            row, col = move
            board[row][col] = PLAYER_O
            new_moves = update_candidate_moves(candidate_moves, (row, col), board)
            eval_score, _ = minimax(board, depth - 1, alpha, beta, False, new_moves, (row, col))
            board[row][col] = EMPTY

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (row, col)

            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break

        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move in sorted_moves:
            row, col = move
            board[row][col] = PLAYER_X
            new_moves = update_candidate_moves(candidate_moves, (row, col), board)
            eval_score, _ = minimax(board, depth - 1, alpha, beta, True, new_moves, (row, col))
            board[row][col] = EMPTY

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (row, col)

            beta = min(beta, eval_score)
            if beta <= alpha:
                break

        return min_eval, best_move

def update_candidate_moves(candidate_moves: Set[Tuple[int, int]], move: Tuple[int, int], board: List[List[str]]) -> Set[Tuple[int, int]]:
    new_moves = set(candidate_moves)
    new_moves.discard(move)
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            nx, ny = move[0] + dx, move[1] + dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[nx][ny] == EMPTY:
                new_moves.add((nx, ny))
    return new_moves

def distance_to(origin: Tuple[int, int], target: Tuple[int, int]) -> int:
    return abs(origin[0] - target[0]) + abs(origin[1] - target[1])

def check_winner_last_move(board, last_move):
    if last_move == (-1, -1):
        return False
    row, col = last_move
    player = board[row][col]
    if player == EMPTY:
        return False

    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        for d in [-1, 1]:
            r, c = row + dr * d, col + dc * d
            while (0 <= r < BOARD_SIZE and 
                   0 <= c < BOARD_SIZE and 
                   board[r][c] == player):
                count += 1
                r += dr * d
                c += dc * d
                if count >= 5:
                    return True
    return False
def evaluate(board):
    score = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == PLAYER_O:
                score += evaluate_position(board, i, j, PLAYER_O)
            elif board[i][j] == PLAYER_X:
                score -= evaluate_position(board, i, j, PLAYER_X)
    return score

def evaluate_position(board, row, col, player):
    directions = [(0,1),(1,0),(1,1),(1,-1)]
    position_score = 0
    for dr, dc in directions:
        line = 1
        # Check both directions
        for d in [-1, 1]:
            r, c = row + dr*d, col + dc*d
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                if board[r][c] == player:
                    line += 1
                elif board[r][c] != EMPTY:
                    break  # Opponent's piece blocks
                else:
                    # Empty space - check if it can form a line
                    if line + 1 >= 5: position_score += 10
                    break
                r += dr*d
                c += dc*d
        if line >= 5: position_score += 1000  # Winning move
        elif line == 4: position_score += 100
        elif line == 3: position_score += 10
    return position_score
