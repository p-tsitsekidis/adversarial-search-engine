# Adversarial Search Engine: Algorithmic Simulation & Performance Analysis

## Overview

A Python-based simulation framework engineered to backtest, benchmark, and profile artificial intelligence algorithms in two-player, zero-sum games (Tic-Tac-Toe and Reversi/Othello). 

This engine explores optimal decision-making, state space traversal, and the strict computational trade-offs between deterministic brute-force search and probabilistic heuristic evaluation. By pitting algorithms against each other in automated arenas, the project provides a quantitative analysis of algorithmic latency, pruning efficiency, and strategic dominance.

## Core Algorithms Implemented

### 1. Deterministic Search: Minimax & Alpha-Beta Pruning
The standard Minimax algorithm explores the entire game tree to find the mathematically optimal move. However, for games with larger state spaces, this becomes computationally unfeasible. 
* **Complexity:** Standard Minimax evaluates $O(b^d)$ nodes, where $b$ is the branching factor and $d$ is the depth.
* **Optimization:** The Alpha-Beta pruning variant dynamically eliminates branches that cannot influence the final decision, significantly reducing the effective branching factor and allowing deeper search within the exact same computational time frame.



### 2. Probabilistic Search: Monte Carlo Tree Search (MCTS)
MCTS diverges from deterministic search by relying on randomized simulations (rollouts) to evaluate the potential of a given move. It elegantly balances **exploration** (trying new moves) and **exploitation** (focusing on moves with a high historical win rate) using the Upper Confidence Bound (UCB1) formula:

$$
UCB1 = \frac{w_i}{n_i} + c \sqrt{\frac{\ln N_i}{n_i}}
$$

(Where $w_i$ is the number of wins, $n_i$ is the node visits, $N_i$ is the parent visits, and $c$ is the exploration parameter).



### 3. Heuristic Approximation: Depth-Limited Minimax
In Reversi, the theoretical state space is roughly $O(10^{28})$, making terminal search impossible. The depth-limited variant introduces a highly tuned **custom heuristic evaluation function** to approximate the utility of non-terminal states. 
* **Reversi Heuristics:** The function evaluates board states using a composite weighted score of *Coin Parity*, *Mobility* (number of legal moves), *Corner Captures*, and a static *Positional Stability Matrix*.



## Simulation & Benchmarking Engine

The core of this project is the simulation engine (`main.py`), which orchestrates automated backtesting of different AI agents against one another over hundreds of trials. 

**Tracked Metrics:**
* **Win/Loss/Draw Rates:** Evaluates the strategic dominance of a given algorithm.
* **Computational Latency:** Tracks the exact execution time per move (`Average_Move_Time`), providing a quantitative measure of algorithmic efficiency and overhead.

### Benchmark Results (MacBook Air)

| Game Environment | Algorithm (Player 1) | Algorithm (Player 2) | Win / Loss / Draw | Avg Move Time (P1) | Avg Move Time (P2) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tic-Tac-Toe** | **Minimax (Pruning)** | Random | 100 / 0 / 0 | 0.0100s | 0.0000s |
| **Tic-Tac-Toe** | MCTS | Random | 96 / 4 / 0 | 0.0150s | 0.0000s |
| **Tic-Tac-Toe** | Minimax (Standard) | **Minimax (Pruning)** | 0 / 0 / 100 | 0.1865s | **0.0011s** |
| **Reversi** | **MCTS** | Limited Pruning | 12 / 4 / 4 | 13.8621s | **0.0655s** |

### Key Algorithmic Insights:
1. **Optimization Impact:** In the *Tic-Tac-Toe* benchmark, Alpha-Beta Pruning (Player 2) achieved the exact same theoretical outcome (Perfect Draw) as Standard Minimax (Player 1) but was approximately **170x faster** (0.0011s vs 0.1865s).
2. **Trade-offs in Large State Spaces:** In *Reversi*, MCTS proved strategically superior (60% win rate) but required significantly higher computational resources (13.8s/move) compared to the fast, heuristic-based Limited Pruning agent (0.06s/move).

## Project Architecture

The codebase relies on strict Object-Oriented encapsulation, separating the game environments from the decision-making agents:
* **`game.py`**: The abstract base class defining environment constraints, state transitions, and utility functions.
* **Environments**: `tictactoe.py` and `reversi.py` inherit from the base class to implement specific state spaces.
* **Agents**: Individual modules (`mcts.py`, `minimax_pruning.py`) contain isolated logic for algorithmic strategies.

## Installation & Usage

1. **Prerequisites:** Python 3.x, `numpy`
2. **Execute Engine:** 
```bash
   python main.py
```

3. Follow the interactive prompts to select the game environment, assign agent algorithms to Player 1 and Player 2, and define the simulation trial count. Performance statistics will print to the console upon completion.

## License

This project is open-source and available under the [MIT License](LICENSE.md).
