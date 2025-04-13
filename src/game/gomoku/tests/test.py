import unittest
from gomoku import create_board, get_empty_positions, player_move, BOARD_SIZE, EMPTY, PLAYER_X, PLAYER_O
from ai import minimax, update_candidate_moves, check_winner_last_move, evaluate

class TestGomoku(unittest.TestCase):
    def setUp(self):
        self.board = create_board()
        self.test_board_win_x = [[EMPTY]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        for i in range(5):  
            self.test_board_win_x[10][10+i] = PLAYER_X
        self.last_move_win = (10, 12)

    # --- Board Logic Tests ---
    def test_create_board(self):
        board = create_board()
        self.assertEqual(len(board), BOARD_SIZE)
        self.assertTrue(all(cell == EMPTY for row in board for cell in row))

    def test_get_empty_positions(self):
        empty_pos = get_empty_positions(self.board)
        self.assertEqual(len(empty_pos), BOARD_SIZE * BOARD_SIZE)
        self.board[0][0] = PLAYER_X
        self.assertEqual(len(get_empty_positions(self.board)), BOARD_SIZE * BOARD_SIZE - 1)

    # --- Win Detection Tests ---
    def test_check_winner_horizontal(self):
        self.assertTrue(check_winner_last_move(self.test_board_win_x, self.last_move_win))

    def test_check_winner_vertical(self):
        test_board = [[EMPTY]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        for i in range(5): 
            test_board[5+i][3] = PLAYER_O
        self.assertTrue(check_winner_last_move(test_board, (7, 3)))

    def test_check_winner_diagonal(self):
        test_board = [[EMPTY]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        for i in range(5):
            test_board[2+i][2+i] = PLAYER_X
        self.assertTrue(check_winner_last_move(test_board, (4, 4)))

    def test_no_winner(self):
        self.assertFalse(check_winner_last_move(self.board, (-1, -1)))

    # --- AI Logic Tests ---
    def test_update_candidate_moves(self):
        candidates = set()
        updated = update_candidate_moves(candidates, (5, 5), self.board)
        self.assertEqual(len(updated), 24)  
        
        edge_updated = update_candidate_moves(candidates, (0, 0), self.board)
        self.assertEqual(len(edge_updated), 12) 

    def test_minimax_terminal_state(self):
        score, _ = minimax(self.test_board_win_x, 3, -1000, 1000, False, set(), self.last_move_win)
        self.assertTrue(score < 0)  

    def test_evaluate_empty_board(self):
        self.assertEqual(evaluate(self.board), 0)

    # --- Integration Tests ---
    def test_ai_blocking_move(self):
        test_board = [[EMPTY]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        for i in range(4):
            test_board[10][10+i] = PLAYER_X
        candidates = update_candidate_moves(set(), (10, 12), test_board)
        _, move = minimax(test_board, 3, -1000, 1000, True, candidates, (10, 12))
        self.assertEqual(move, (10, 14))  

class TestEdgeCases(unittest.TestCase):
    def test_board_edge_win(self):
        board = [[EMPTY]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        for i in range(5):  
            board[0][10+i] = PLAYER_X
        self.assertTrue(check_winner_last_move(board, (0, 12)))

    def test_full_board_no_winner(self):
        board = [[PLAYER_X if (i+j) % 2 == 0 else PLAYER_O for j in range(BOARD_SIZE)] 
                for i in range(BOARD_SIZE)]
        self.assertFalse(check_winner_last_move(board, (BOARD_SIZE-1, BOARD_SIZE-1)))
        self.assertEqual(len(get_empty_positions(board)), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
