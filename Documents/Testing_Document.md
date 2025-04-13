
### What was tested?
- **Board Logic Tests**:
  - Creation of the game board.
  - Getting empty positions on the board.
  
- **Win Detection Tests**:
  - Horizontal win detection.
  - Vertical win detection.
  - Diagonal win detection.
  - No winner scenario.
  
- **AI Logic Tests**:
  - Updating candidate moves for AI.
  - Minimax algorithm in terminal state.
  - Evaluation of an empty board.
  
- **Integration Tests**:
  - AI blocking move logic.

- **Edge Cases**:
  - Win detection on the edge of the board.
  - Full board with no winner scenario.

### Types of Inputs Used for Testing
- **Empty board** and partially filled boards with specific players (`PLAYER_X` and `PLAYER_O`).
- Test cases involving winning combinations (horizontal, vertical, diagonal).
- Random moves for testing AI strategies.
- Fully filled boards with alternating player moves.
