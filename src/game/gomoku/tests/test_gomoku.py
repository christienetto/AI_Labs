import unittest
import numpy as np
from ai import minimax, check_win, best_move

class TestGomoku(unittest.TestCase):
    
    def test_check_win_horizontal(self):
        board = np.full((20, 20), '.', dtype=str)
        for i in range(5):
            board[5, i] = 'X'
        self.assertTrue(check_win(board, 'X'))
        self.assertFalse(check_win(board, 'O'))

    def test_check_win_vertical(self):
        board = np.full((20, 20), '.', dtype=str)
        for i in range(5):
            board[i, 7] = 'O'
        self.assertTrue(check_win(board, 'O'))
        self.assertFalse(check_win(board, 'X'))

    def test_best_move(self):
        board = np.full((20, 20), '.', dtype=str)
        board[10, 10] = 'X'
        move = best_move(board)
        self.assertIn(move, [(9, 9), (9, 10), (10, 9), (11, 11)])  

    def test_minimax(self):
        board = np.full((20, 20), '.', dtype=str)
        board[0, 0] = 'X'
        board[1, 1] = 'O'
        score, move = minimax(board, 2, True, {(0, 0), (1, 1)})  
        self.assertIsInstance(score, int)
        self.assertIsInstance(move, tuple)
        self.assertEqual(len(move), 2)

if __name__ == '__main__':
    unittest.main()

