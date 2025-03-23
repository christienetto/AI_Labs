

# Project Progress and Details

## 1. Which programming language are you using?
I am using Python as the main programming language for my project since I am more familiar with it compared to others. The UI will be implemented using Tkinter for a simple and interactive interface.

## 2. Also, mention any other languages you are proficient in to the extent that you could peer-review projects written in them.
I am proficient in Go Golang, JavaScript with Svelte and Next.js, and SQL with tools like SQLC. I would feel confident reviewing projects written in these languages.

## 3. What algorithms and data structures will you implement in your project?
The project will use the Minimax algorithm with Alpha-Beta Pruning to improve efficiency in searching the game tree for the best possible move. The main data structure will be a 2D array, and a game tree will be used for AI decision-making.

## 4. What problem are you solving?
The goal of the project is to develop an AI opponent for the game Gomoku, which makes optimal moves using the Minimax algorithm with Alpha-Beta Pruning.

## 5. What inputs does the program receive, and how are they used?

Player moves via input by clicking the board and the movement of AI from a minimax algorithm.

## 6. Expected time and space complexities (e.g., Big-O analysis)
Minimax Time Complexity: O(b^d)

Minimax with Alpha-Beta Pruning Time Complexity: O(b^(d/2))

Minimax Space Complexity: O(bd)
## 7. Find out as much as possible. You are not expected to prove or measure anything yourself.
I will study Alpha-Beta Pruning optimizations to speed up the AI's decision-making process. Additionally, I will research heuristic evaluation functions to improve move selection.

## 8. Use time and space complexity as a tool to understand how to approach the project.

## 9. Check Wikipedia or other reliable sources, and ensure you understand where these complexities come from in your algorithm. Why does your algorithm require that amount of time?

- Time complexity: The Minimax algorithm runs in O(b^d) time, where b is the branching factor (number of possible moves) and d is the search depth. Using Alpha-Beta Pruning significantly reduces this complexity by eliminating unnecessary searches, making it closer to O(b^(d/2)).
- Space complexity: The game tree requires O(bd) space to store nodes during search, but this can be optimized by limiting search depth and using iterative deepening. 

## 10. References
- Wikipedia: Minimax algorithm
- Wikipedia: Alpha-Beta Pruning
- Python Tkinter documentation

Core of the Project: The project is an AI-driven Gomoku game where the AI opponent uses Minimax with Alpha-Beta Pruning to play optimally against a human player.
