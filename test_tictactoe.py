"""
Test suite for the Tic-Tac-Toe game using unittest.
"""

import unittest
from unittest.mock import patch
import tictactoe


class TestBoardInitialization(unittest.TestCase):
    """Tests for board initialization and reset."""
    
    def test_initialize_board_creates_empty_board(self):
        board = tictactoe.initialize_board()
        self.assertEqual(len(board), 9)
        for i in range(1, 10):
            self.assertIsNone(board[i])
    
    def test_initialize_board_has_correct_keys(self):
        board = tictactoe.initialize_board()
        self.assertEqual(set(board.keys()), set(range(1, 10)))
    
    def test_reset_board_clears_all_squares(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[5] = 'O'
        board[9] = 'X'
        board = tictactoe.reset_board(board)
        for i in range(1, 10):
            self.assertIsNone(board[i])


class TestBoardDisplay(unittest.TestCase):
    """Tests for board display functionality."""
    
    def test_display_board_empty(self):
        board = tictactoe.initialize_board()
        with patch('builtins.print'):
            tictactoe.display_board(board)
    
    def test_display_board_with_marks(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[5] = 'O'
        board[9] = 'X'
        with patch('builtins.print'):
            tictactoe.display_board(board)


class TestMoveValidation(unittest.TestCase):
    """Tests for move validation."""
    
    def test_validate_move_empty_square(self):
        board = tictactoe.initialize_board()
        self.assertTrue(tictactoe.validate_move(board, 1))
        self.assertTrue(tictactoe.validate_move(board, 5))
        self.assertTrue(tictactoe.validate_move(board, 9))
    
    def test_validate_move_occupied_square(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[5] = 'O'
        self.assertFalse(tictactoe.validate_move(board, 1))
        self.assertFalse(tictactoe.validate_move(board, 5))
    
    def test_validate_move_out_of_range(self):
        board = tictactoe.initialize_board()
        self.assertFalse(tictactoe.validate_move(board, 0))
        self.assertFalse(tictactoe.validate_move(board, 10))
        self.assertFalse(tictactoe.validate_move(board, -1))
    
    def test_validate_move_non_integer(self):
        board = tictactoe.initialize_board()
        self.assertFalse(tictactoe.validate_move(board, "5"))
        self.assertFalse(tictactoe.validate_move(board, 5.5))
        self.assertFalse(tictactoe.validate_move(board, None))


class TestPlayerInput(unittest.TestCase):
    """Tests for getting and processing player input."""
    
    def test_get_player_move_valid_input(self):
        board = tictactoe.initialize_board()
        with patch('builtins.input', return_value='5'):
            move = tictactoe.get_player_move(board, 'X')
            self.assertEqual(move, 5)
    
    def test_get_player_move_string_number(self):
        board = tictactoe.initialize_board()
        with patch('builtins.input', return_value='7'):
            move = tictactoe.get_player_move(board, 'X')
            self.assertEqual(move, 7)
    
    def test_get_player_move_invalid_then_valid(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        with patch('builtins.input', side_effect=['1', '2']):
            with patch('builtins.print'):
                move = tictactoe.get_player_move(board, 'O')
                self.assertEqual(move, 2)
    
    def test_get_player_move_quit_command(self):
        board = tictactoe.initialize_board()
        with patch('builtins.input', return_value='q'):
            with self.assertRaises(tictactoe.QuitGame):
                tictactoe.get_player_move(board, 'X')
    
    def test_get_player_move_quit_uppercase(self):
        board = tictactoe.initialize_board()
        with patch('builtins.input', return_value='Q'):
            with self.assertRaises(tictactoe.QuitGame):
                tictactoe.get_player_move(board, 'X')


class TestPlaceMove(unittest.TestCase):
    """Tests for placing moves on the board."""
    
    def test_place_move_x(self):
        board = tictactoe.initialize_board()
        tictactoe.place_move(board, 1, 'X')
        self.assertEqual(board[1], 'X')
    
    def test_place_move_o(self):
        board = tictactoe.initialize_board()
        tictactoe.place_move(board, 5, 'O')
        self.assertEqual(board[5], 'O')
    
    def test_place_move_multiple(self):
        board = tictactoe.initialize_board()
        tictactoe.place_move(board, 1, 'X')
        tictactoe.place_move(board, 2, 'O')
        tictactoe.place_move(board, 3, 'X')
        self.assertEqual(board[1], 'X')
        self.assertEqual(board[2], 'O')
        self.assertEqual(board[3], 'X')
        self.assertIsNone(board[4])


class TestWinDetection(unittest.TestCase):
    """Tests for win detection."""
    
    def test_win_row_1(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[2] = 'X'
        board[3] = 'X'
        self.assertTrue(tictactoe.check_win(board, 'X'))
    
    def test_win_row_2(self):
        board = tictactoe.initialize_board()
        board[4] = 'O'
        board[5] = 'O'
        board[6] = 'O'
        self.assertTrue(tictactoe.check_win(board, 'O'))
    
    def test_win_row_3(self):
        board = tictactoe.initialize_board()
        board[7] = 'X'
        board[8] = 'X'
        board[9] = 'X'
        self.assertTrue(tictactoe.check_win(board, 'X'))
    
    def test_win_column_1(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[4] = 'X'
        board[7] = 'X'
        self.assertTrue(tictactoe.check_win(board, 'X'))
    
    def test_win_column_2(self):
        board = tictactoe.initialize_board()
        board[2] = 'O'
        board[5] = 'O'
        board[8] = 'O'
        self.assertTrue(tictactoe.check_win(board, 'O'))
    
    def test_win_column_3(self):
        board = tictactoe.initialize_board()
        board[3] = 'X'
        board[6] = 'X'
        board[9] = 'X'
        self.assertTrue(tictactoe.check_win(board, 'X'))
    
    def test_win_diagonal_1(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[5] = 'X'
        board[9] = 'X'
        self.assertTrue(tictactoe.check_win(board, 'X'))
    
    def test_win_diagonal_2(self):
        board = tictactoe.initialize_board()
        board[3] = 'O'
        board[5] = 'O'
        board[7] = 'O'
        self.assertTrue(tictactoe.check_win(board, 'O'))
    
    def test_no_win_incomplete_row(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[2] = 'X'
        self.assertFalse(tictactoe.check_win(board, 'X'))
    
    def test_no_win_mixed_marks(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[2] = 'X'
        board[3] = 'O'
        self.assertFalse(tictactoe.check_win(board, 'X'))
    
    def test_no_win_empty_board(self):
        board = tictactoe.initialize_board()
        self.assertFalse(tictactoe.check_win(board, 'X'))
        self.assertFalse(tictactoe.check_win(board, 'O'))


class TestDrawDetection(unittest.TestCase):
    """Tests for draw detection."""
    
    def test_draw_full_board(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[2] = 'O'
        board[3] = 'X'
        board[4] = 'O'
        board[5] = 'X'
        board[6] = 'X'
        board[7] = 'O'
        board[8] = 'X'
        board[9] = 'O'
        self.assertTrue(tictactoe.check_draw(board))
    
    def test_no_draw_not_full(self):
        board = tictactoe.initialize_board()
        board[1] = 'X'
        board[2] = 'O'
        board[3] = 'X'
        self.assertFalse(tictactoe.check_draw(board))
    
    def test_no_draw_empty_board(self):
        board = tictactoe.initialize_board()
        self.assertFalse(tictactoe.check_draw(board))


class TestPlayAgainPrompt(unittest.TestCase):
    """Tests for the play again prompt."""
    
    def test_play_again_yes(self):
        with patch('builtins.input', return_value='yes'):
            self.assertTrue(tictactoe.play_again_prompt())
    
    def test_play_again_y(self):
        with patch('builtins.input', return_value='y'):
            self.assertTrue(tictactoe.play_again_prompt())
    
    def test_play_again_no(self):
        with patch('builtins.input', return_value='no'):
            self.assertFalse(tictactoe.play_again_prompt())
    
    def test_play_again_n(self):
        with patch('builtins.input', return_value='n'):
            self.assertFalse(tictactoe.play_again_prompt())
    
    def test_play_again_invalid_then_yes(self):
        with patch('builtins.input', side_effect=['maybe', 'yes']):
            with patch('builtins.print'):
                self.assertTrue(tictactoe.play_again_prompt())


class TestIntegration(unittest.TestCase):
    """Integration tests for complete game scenarios."""
    
    def test_x_wins_row(self):
        board = tictactoe.initialize_board()
        tictactoe.place_move(board, 1, 'X')
        tictactoe.place_move(board, 4, 'O')
        tictactoe.place_move(board, 2, 'X')
        tictactoe.place_move(board, 5, 'O')
        tictactoe.place_move(board, 3, 'X')
        self.assertTrue(tictactoe.check_win(board, 'X'))
        self.assertFalse(tictactoe.check_win(board, 'O'))
    
    def test_o_wins_diagonal(self):
        board = tictactoe.initialize_board()
        tictactoe.place_move(board, 1, 'X')
        tictactoe.place_move(board, 3, 'O')
        tictactoe.place_move(board, 2, 'X')
        tictactoe.place_move(board, 5, 'O')
        tictactoe.place_move(board, 4, 'X')
        tictactoe.place_move(board, 7, 'O')
        self.assertTrue(tictactoe.check_win(board, 'O'))
        self.assertFalse(tictactoe.check_win(board, 'X'))
    
    def test_draw_game(self):
        board = tictactoe.initialize_board()
        moves = [
            (1, 'X'), (2, 'O'), (3, 'X'),
            (5, 'O'), (4, 'X'), (6, 'O'),
            (8, 'X'), (7, 'O'), (9, 'X')
        ]
        for square, player in moves:
            tictactoe.place_move(board, square, player)
        self.assertTrue(tictactoe.check_draw(board))
        self.assertFalse(tictactoe.check_win(board, 'X'))
        self.assertFalse(tictactoe.check_win(board, 'O'))


if __name__ == '__main__':
    unittest.main()
