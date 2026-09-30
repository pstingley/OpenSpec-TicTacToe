# Terminal Tic-Tac-Toe Game

A classic two-player Tic-Tac-Toe game implemented in Python and playable in the terminal.

## Overview

This project provides a complete, playable Tic-Tac-Toe game where two human players can compete against each other in the terminal. The game includes clear board display, input validation, win detection, draw detection, and the ability to play multiple games in succession.

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Installation

Simply clone or download this repository. No installation or dependencies are required beyond Python itself.

```bash
git clone <repository-url>
cd OpenSpec-TicTacToe
```

## Running the Game

To start a game, run:

```bash
python tictactoe.py
```

## Gameplay Instructions

### How to Play

1. **Starting the Game**: When you start the game, both players will see the game board with squares numbered 1-9
2. **Board Layout**: The board is displayed in a 3x3 grid:
   ```
   1 | 2 | 3
   --+---+--
   4 | 5 | 6
   --+---+--
   7 | 8 | 9
   ```

3. **Taking Turns**: 
   - Player X always goes first
   - Players alternate turns
   - When prompted, enter the number (1-9) of the square where you want to place your mark

4. **Valid Moves**:
   - Enter a number from 1 to 9
   - You can only move to empty squares
   - If you try to move to an occupied square, the game will reject your move and ask again
   - If you enter invalid input, you'll see an error message and can try again

5. **Special Commands**:
   - Enter 'q' at any time to quit the game immediately
   - Enter 'q' or 'Q' to exit without playing again

### Game Outcomes

**Winning**: If you get three of your marks (X or O) in a row, column, or diagonal, you win! The game will announce the winner.

**Draw**: If all 9 squares are filled and neither player has won, the game is a draw.

**Play Again**: After each game ends, you'll be asked if you want to play another game:
   - Enter 'yes' or 'y' to play again (the board resets)
   - Enter 'no' or 'n' to quit

### Example Game Flow

```
Player X's turn. Enter move (1-9) or 'q' to quit: 5

1 | 2 | 3
--+---+--
4 | X | 6
--+---+--
7 | 8 | 9

Player O's turn. Enter move (1-9) or 'q' to quit: 1
```

## Game Mechanics

### Win Conditions
A player wins by placing three of their marks in any of these patterns:
- **Rows**: Top (1-2-3), Middle (4-5-6), or Bottom (7-8-9)
- **Columns**: Left (1-4-7), Middle (2-5-8), or Right (3-6-9)
- **Diagonals**: Top-left to bottom-right (1-5-9) or Top-right to bottom-left (3-5-7)

### Draw Condition
A draw occurs when all 9 squares are filled and neither player has achieved three in a row.

### Turn Order
- X plays first (always)
- Players alternate turns
- The game ends when someone wins or the board fills up (draw)

## Running Tests

This project includes comprehensive automated tests. To run the test suite:

```bash
python -m unittest test_tictactoe -v
```

This will run all 39 unit and integration tests covering:
- Board initialization and reset
- Board display
- Move validation
- Player input handling
- Move placement
- Win detection (rows, columns, diagonals)
- Draw detection
- Play-again prompts
- Complete game scenarios

### Expected Test Output

```
Ran 39 tests in 0.007s

OK
```

All tests should pass, covering:
- ✓ 39 total test cases
- ✓ 100% coverage of core game logic
- ✓ Input validation and error handling
- ✓ Win and draw detection
- ✓ Complete game integration scenarios

## Project Structure

```
OpenSpec-TicTacToe/
├── tictactoe.py           # Main game implementation
├── test_tictactoe.py      # Comprehensive test suite
├── README.md              # This file
└── openspec/              # OpenSpec change artifacts
    └── changes/
        └── build-terminal-tictactoe-game/
            ├── proposal.md
            ├── design.md
            ├── tasks.md
            └── specs/
```

## Code Architecture

### Core Modules

**tictactoe.py** provides these main functions:

- `initialize_board()`: Creates an empty 3x3 board
- `reset_board(board)`: Clears the board for a new game
- `display_board(board)`: Shows the current board state
- `validate_move(board, move)`: Checks if a move is valid
- `get_player_move(board, player)`: Gets and validates player input
- `place_move(board, move, player)`: Places a move on the board
- `check_win(board, player)`: Detects if a player has won
- `check_draw(board)`: Detects if the game is a draw
- `play_again_prompt()`: Asks if players want to continue
- `play_game()`: Manages a single game session
- `main()`: Orchestrates overall game flow

### Key Features

- **Robust Input Validation**: Rejects invalid moves and out-of-range inputs with clear error messages
- **Complete Win Detection**: Checks all 8 winning combinations (3 rows + 3 columns + 2 diagonals)
- **Draw Detection**: Identifies when the board is full with no winner
- **User-Friendly**: Clear board display after each move, helpful prompts, and informative error messages
- **Multiple Games**: Players can easily play multiple games in one session with the "play again" feature
- **Quit Anytime**: Enter 'q' to exit immediately during gameplay

## Testing Coverage

The test suite covers:

### Unit Tests
- Board initialization with correct structure
- Board display functionality
- Move validation (valid moves, occupied squares, out-of-range, non-numeric)
- Player input handling and quit command recognition
- Move placement on the board
- Win detection for all row, column, and diagonal combinations
- Draw detection

### Integration Tests
- Complete game scenarios (X wins, O wins, draw)
- Multiple consecutive games
- Error recovery and retry logic

## Future Enhancements

Possible future improvements (not implemented in this version):
- AI opponent
- Graphical user interface
- Game statistics and history
- Network multiplayer
- Different difficulty levels

## Troubleshooting

**Game won't start**: Ensure you have Python 3.6+ installed
- Check with: `python --version`

**Tests won't run**: Make sure you're in the project directory
- Run: `cd OpenSpec-TicTacToe`
- Then: `python -m unittest test_tictactoe -v`

**Input not being recognized**: Make sure to:
- Enter numbers 1-9 for moves (not 0 or 10)
- Enter 'q' to quit (not other letters)
- Enter 'yes', 'y', 'no', or 'n' for play-again prompts

## License

This project is provided as-is for educational purposes.

## Author

Developed as part of CIS 890 - System Specification coursework using OpenSpec methodology.
