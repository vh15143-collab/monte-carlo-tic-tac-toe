# Monte Carlo Tic-Tac-Toe Using MCTS

## 1. Problem

Tic-Tac-Toe is a two-player game played on a 3 × 3 board. The objective of this project is to develop an Artificial Intelligence-based Tic-Tac-Toe game where two different AI techniques make decisions automatically.

The project uses:

* **Monte Carlo Tree Search (MCTS)** for player X
* **Minimax Algorithm** for player O

The main goal is to demonstrate and compare two different AI decision-making approaches in a simple game environment.

---

## 2. Approach

### Monte Carlo Tree Search (MCTS)

MCTS selects moves by performing multiple simulations.

The main steps are:

1. **Selection** – Select a promising node using UCT.
2. **Expansion** – Add a new node for an unexplored move.
3. **Simulation** – Play random moves until the game ends.
4. **Backpropagation** – Update the results back through the tree.

The project uses **500 simulations** for each MCTS move.

### Minimax

Minimax examines possible future game states and selects a suitable move assuming that the opponent also makes the best possible decision.

In this project:

```text
MCTS    → Player X
Minimax → Player O
```

---

## 3. Project Structure

```text
monte-carlo-tic-tac-toe/
│
├── src/
│   ├── tictactoe.py
│   ├── mcts.py
│   ├── minimax.py
│   └── main.py
│
├── test/
│   └── test_games.py
│
├── docs/
│   └── report.md
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 4. Requirements

* Python 3.x
* IntelliJ IDEA or any Python IDE
* Git

No external Python packages are required.

---

## 5. How to Run

### Step 1: Open the project

Open the `monte-carlo-tic-tac-toe` project in IntelliJ IDEA.

### Step 2: Run the main program

Open:

```text
src/main.py
```

Run the file using the Python interpreter.

Alternatively, from the project root, run:

```bash
python src/main.py
```

### Step 3: Run the tests

To run the test file:

```bash
python test/test_games.py
```

---

## 6. Sample Input

The project does not require an external input file.

The Tic-Tac-Toe board is created automatically:

```text
   |   |
---+---+---
   |   |
---+---+---
   |   |
```

The board contains nine positions:

```text
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

---

## 7. Sample Output

An example of the MCTS test output is:

```text
Initial Tic-Tac-Toe Board:

   |   |
---+---+---
   |   |
---+---+---
   |   |

MCTS selected move: 5
Total simulations: 500

Board after MCTS move:

   |   |
---+---+---
   | X |
---+---+---
   |   |
```

The complete game then allows Minimax to make the move for player O and continues until there is a winner or a draw.

---

## 8. Testing Output

Example test execution:

```text
Running Tic-Tac-Toe Tests
-------------------------
Tic-Tac-Toe test passed
MCTS test passed
MCTS selected move: 5
Total simulations: 500
Minimax test passed
-------------------------
All tests passed successfully!
```

---

## 9. Result

The project successfully demonstrates automated Tic-Tac-Toe gameplay using MCTS and Minimax. MCTS uses simulations to explore possible moves, while Minimax evaluates future game states to make decisions.

---

## 10. Future Enhancements

* Add Human vs AI mode.
* Add a graphical user interface.
* Add different difficulty levels.
* Record game statistics.
* Compare MCTS and Minimax over multiple games.
* Display the MCTS search tree.
