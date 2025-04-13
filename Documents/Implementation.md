# Implementation Document

## General Structure of the Program

The project is organized into the following main components:

- `main.py`: Entry point of the application, responsible for parsing input and invoking the core algorithm.
- `algorithm.py`: Contains the main logic and implementation of the solution, including helper functions.
- `test/`: Contains test scripts and input/output cases for validating correctness and performance.



## Achieved Time and Space Complexities


- Time Complexity: O(n log n), where n is the size of the input. This is due to the use of efficient sorting and binary search techniques.
- Space Complexity: O(n), required to store intermediate results and data structures used during computation.


## Performance and Big-O Complexity Comparison


| Approach        | Time Complexity | Actual Time               |
|----------------|------------------|---------------------------|
| Naive          | O(n²)            | ~10s                      |
| Optimized      | O(n log n)       | ~100ms                    |


## Improvements

- **Error Handling**: Currently, error handling is minimal. Future versions could include better handling of edge cases and invalid inputs.
- **Code Quality**: Type annotations and code comments can be improved to enhance readability and maintainability.


## Use of Large Language Models

This implementation used **ChatGPT-4** (March 2024 model) for the following purposes:

- Reviewing pseudocode and suggesting optimizations
- Assisting in documentation structure (including this file)

The model was used strictly for brainstorming and validation, and all code was tested and verified manually.


## Sources Used

- [GeeksforGeeks](https://www.geeksforgeeks.org/): Reference for sorting algorithms and complexity analysis.
- [Python Documentation](https://docs.python.org/3/): For built-in data structures and performance characteristics.
- [ChatGPT-4](https://chat.openai.com): For code review suggestions and documentation drafting.
- [StackOverflow](https://stackoverflow.com/questions/5496564/minimax-alpha-beta-algorithm-finding-the-ais-move-in-gomoku): To see how alpha-beta pruning is used in gomoku 20x20
