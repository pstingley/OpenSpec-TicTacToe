# Design

## Context

See proposal.md for motivation and overall scope. This design focuses on the architecture and implementation approach for the terminal-based Tic-Tac-Toe game.

## Goals / Non-Goals

**Goals:**
- Implement a complete, playable Tic-Tac-Toe game with a clear, user-friendly terminal interface
- Ensure robust input validation and error handling
- Provide comprehensive test coverage for all game mechanics
- Create clear, maintainable code with well-documented functions
- Deliver with full documentation for users and developers

**Non-Goals:**
- Graphical user interface (this is terminal-only)
- Network/multiplayer capabilities beyond local two-player
- AI opponent (only human vs human)
- Game difficulty levels or variants
- Persistent game state or replay history
- Win/loss statistics tracking

## Decisions

### 1. Board Representation and State Management
**Decision**: Represent the board as a dictionary mapping square numbers (1-9) to player marks ('X', 'O', or None for empty).

**Rationale**: Dictionaries provide O(1) lookup time for checking individual squares, making win detection efficient. The mapping is intuitive and directly corresponds to the numbered squares players see on screen. This avoids the overhead of a 2D array and the need for coordinate conversion.

**Alternatives considered**:
- 2D list/array: Would require coordinate conversion and more complex indexing for win detection
- Simple list of 9 elements: Works but less intuitive since square numbers 1-9 don't naturally map to indices 0-8

### 2. Game Loop Structure
**Decision**: Use an outer loop for multiple games (play again) and an inner loop for turns within a single game.

**Rationale**: Cleanly separates concerns - the outer loop handles game lifecycle (new game, play again, quit), while the inner loop manages turn flow (whose turn, get move, update board, check win/draw). This structure makes it easy to reset the board between games without reinitializing the entire game state.

**Alternatives considered**:
- Single loop with complex conditional logic: Would be harder to read and maintain
- Recursive game calls: Unnecessary complexity for this use case

### 3. Win Detection Algorithm
**Decision**: Define all eight winning combinations (three rows, three columns, two diagonals) and check if any player has all three squares of any combination.

**Rationale**: Simple, explicit, and easy to test. With only eight combinations and nine squares, a lookup-based approach is faster than algorithmic checks and more maintainable than mathematical formulas. This approach makes each win condition testable independently.

**Alternatives considered**:
- Mathematical/algorithmic checks based on square positions: More elegant but harder to understand and debug
- Minimax or advanced game tree evaluation: Unnecessary for simple win detection

### 4. Input Validation
**Decision**: Validate input in a dedicated function that checks for:
1. Non-empty input
2. Numeric value (1-9) or quit command ('q')
3. Square is not already occupied

**Rationale**: Separates input handling from game logic, making both easier to test and maintain. Centralized validation ensures consistent error messages and reduces bugs from scattered validation logic.

**Alternatives considered**:
- Inline validation in the main game loop: Would make the loop harder to read
- Try-catch error handling: Python's exception-based flow would be overkill for expected validation failures

### 5. User Feedback and Prompts
**Decision**: Display the board after each move and provide clear prompts showing whose turn it is, what input is expected, and error messages for invalid moves.

**Rationale**: Frequent visual feedback keeps players oriented and confident in the game state. Clear prompts reduce confusion about what input is expected. Specific error messages help players correct their mistakes immediately.

**Alternatives considered**:
- Minimal output (only at game end): Makes gameplay confusing and frustrating
- Verbose output: Would clutter the terminal without improving usability

### 6. File Structure and Separation
**Decision**: Implement core game logic in `tictactoe.py` with clear function boundaries (board management, move validation, win detection, game loop). Keep tests in a separate `test_tictactoe.py` file.

**Rationale**: Separating logic from test code makes both easier to maintain and allows the game to be imported as a module. Clear function boundaries make individual components testable in isolation.

**Alternatives considered**:
- Single monolithic script: Harder to test and reuse components
- Multiple files for different concerns: Overkill for the game's current scope, but structure allows future growth

## Risks / Trade-offs

**Risk**: Player confusion about coordinate system (numbers vs grid layout)
→ **Mitigation**: Display board clearly with numbered positions on each game turn; include instructions in README

**Risk**: Edge cases in input validation
→ **Mitigation**: Comprehensive test coverage with pytest for all input scenarios

**Risk**: Complex win-checking logic could have bugs
→ **Mitigation**: Explicit list of winning combinations with individual test cases for each; visual board display after each move lets players spot errors immediately

**Trade-off**: Using dictionaries vs arrays adds slight memory overhead but gains code clarity and testability
→ **Accepted**: Clarity and correctness are more important than minor memory efficiency for this application

**Trade-off**: Immediate game reset after "play again" rather than state review
→ **Accepted**: Aligns with quick-play use case; players can review if needed before restarting
