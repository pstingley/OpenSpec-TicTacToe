# Tasks

## 1. Core Game Infrastructure

- [x] 1.1 Create `tictactoe.py` module with board initialization function that creates an empty board as a dictionary mapping positions 1-9 to None; verify by importing the module and testing that calling the initialization function returns the correct data structure

- [x] 1.2 Implement function to reset/clear the board; verify with unit tests that the function returns all squares to None state

- [x] 1.3 Implement board display function that renders the current board state in a 3x3 grid format with numbered squares for empty positions and X/O marks for occupied positions; verify by visual inspection and unit tests with various board states

## 2. Move Validation and Input Handling

- [x] 2.1 Implement `validate_move()` function that checks if a move is valid (square number 1-9 and not already occupied); verify with unit tests covering valid moves, invalid numbers, empty squares, and occupied squares

- [x] 2.2 Implement `get_player_move()` function that prompts the current player for input and returns the validated move; verify with unit tests that it accepts valid moves (1-9) and rejects invalid input with appropriate error messages

- [x] 2.3 Add support for 'q' quit command in input handling; verify with unit tests that entering 'q' at any prompt is properly recognized and triggers game exit

- [x] 2.4 Implement `place_move()` function that updates the board with a player's mark at the specified position; verify with unit tests that moves are placed correctly and the board state updates as expected

## 3. Win Detection

- [x] 3.1 Implement `check_win()` function that checks all eight winning combinations (three rows, three columns, two diagonals) and returns True if the current player has won; verify with unit tests for each row win

- [x] 3.2 Add tests for column win detection; verify all three column combinations are tested and pass

- [x] 3.3 Add tests for diagonal win detection; verify both diagonal combinations are tested and pass

- [x] 3.4 Verify `check_win()` returns False when no win condition is met; verify with unit tests for partial boards and boards with marks from both players

## 4. Draw Detection

- [x] 4.1 Implement `check_draw()` function that returns True if the board is full and no player has won; verify with unit tests that it correctly identifies a full board with no winner

- [x] 4.2 Verify `check_draw()` returns False when the board is not full; verify with unit tests for boards with empty squares

- [x] 4.3 Verify `check_draw()` returns False when a player has won; verify with unit tests that it distinguishes wins from draws

## 5. Game Loop and Turn Management

- [x] 5.1 Implement `play_game()` function that manages a single game session with turn alternation between X and O, starting with X; verify with integration tests that simulate a complete game from start to finish

- [x] 5.2 Implement turn logic that correctly alternates between players and prompts the appropriate player for their move; verify with unit tests that the player indicator changes correctly after each move

- [x] 5.3 Implement game end detection that stops the game when a win or draw occurs; verify with integration tests that simulate games ending in wins and draws

- [x] 5.4 Implement `play_again_prompt()` function that asks players if they want to play another game and returns their response; verify with unit tests for yes/no/invalid responses

## 6. User Interface and Feedback

- [x] 6.1 Add welcome message and game instructions displayed at startup; verify by running the game and observing the startup messages

- [x] 6.2 Implement clear player turn prompts that display which player's turn it is and request a valid move (1-9 or 'q'); verify by visual inspection during gameplay

- [x] 6.3 Add error messages for invalid input and occupied squares with specific, helpful text; verify by attempting invalid moves and checking that error messages appear and are clear

- [x] 6.4 Implement game end messages that display the winner or announce a draw; verify by running test games and checking the end-game output

- [x] 6.5 Display the board after each move to show current game state; verify by visual inspection during gameplay that the board updates correctly

## 7. Main Entry Point and Game Flow

- [x] 7.1 Implement `main()` function that orchestrates the overall game flow: welcome message, play games in a loop, handle play-again responses, and support quit command; verify by running the game end-to-end and playing multiple games with both win and quit scenarios

- [x] 7.2 Add `if __name__ == "__main__":` block that calls main() to make the module executable; verify by running `python tictactoe.py` from the command line

## 8. Comprehensive Test Suite

- [x] 8.1 Create `test_tictactoe.py` and implement tests for board initialization and reset; verify by running `pytest test_tictactoe.py::test_board*` and checking that all tests pass

- [x] 8.2 Implement tests for move validation covering all scenarios (valid moves, invalid numbers, occupied squares, non-numeric input); verify by running `pytest test_tictactoe.py::test_validate_move*` and checking that all tests pass

- [x] 8.3 Implement tests for win detection covering rows, columns, and diagonals; verify by running `pytest test_tictactoe.py::test_*win*` and checking that all tests pass

- [x] 8.4 Implement tests for draw detection; verify by running `pytest test_tictactoe.py::test_draw*` and checking that all tests pass

- [x] 8.5 Implement integration tests simulating complete game scenarios (X wins, O wins, draw); verify by running `pytest test_tictactoe.py` and ensuring all tests pass with 100% test coverage for game logic

- [x] 8.6 Run full test suite and verify all tests pass; verify by running `pytest test_tictactoe.py -v` with zero failures

## 9. Documentation

- [x] 9.1 Create `README.md` with project overview, requirements, and installation instructions; verify by checking that the README describes the game and any setup steps

- [x] 9.2 Add gameplay instructions to README explaining how to run the game, how to enter moves (numbers 1-9), how to quit (q), and describing the board numbering; verify by reading the README and confirming it's clear enough for a new player to start the game

- [x] 9.3 Document the game mechanics in README (turn order, win conditions, draw condition, play again); verify by checking that a new player can understand the game rules from the README

- [x] 9.4 Add testing instructions to README showing how to run tests with pytest; verify by running the command exactly as documented and checking that it works

## 10. Final Integration and Verification

- [x] 10.1 Run the game manually and play a complete game to X win, then play again to O win, then quit; verify by observing correct gameplay flow, accurate board state, correct winner detection, and proper quit handling

- [x] 10.2 Test edge cases: attempts to move to occupied squares, invalid input (letters, out-of-range numbers), and multiple play-again cycles; verify by testing each scenario and confirming proper error messages and game behavior

- [x] 10.3 Run full test suite and confirm all tests pass; verify by running `pytest test_tictactoe.py` with zero failures and all game logic covered
