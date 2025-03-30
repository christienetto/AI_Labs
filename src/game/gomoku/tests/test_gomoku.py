import unittest
import numpy as np
from ai import minimax, check_win, best_move

class TestGomoku(unittest.TestCase):
    
    def test_check_win(self):
        # Testing a horizontal win for Player X
        board = np.array([
            ['X', 'X', 'X', 'X', 'X'] + ['.']*15,
            ['.', '.', '.', '.', '.']*4
        ])
        self.assertTrue(check_win(board, 'X'))
        self.assertFalse(check_win(board, 'O'))

    def test_best_move(self):
        board = np.full((20, 20), '.', dtype=str)
        board[10, 10] = 'X'  # Placing a piece for Player X
        move = best_move(board)
        self.assertEqual(move, (9, 9))  # AI will likely choose the adjacent empty spot

    def test_minimax(self):
        board = np.array([
            ['X', 'X', '.', '.', '.'],
            ['.', 'O', '.', '.', '.'],
            ['.', '.', 'X', '.', '.'],
            ['.', '.', '.', 'O', '.'],
            ['.', '.', '.', '.', '.']
        ])
        result = minimax(board, 3, True)  # AI's turn
        self.assertIsInstance(result, int)  # Should return an integer score

if __name__ == '__main__':
    unittest.main()

