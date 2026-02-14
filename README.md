# AI Game Strategies: Algorithmic Simulation & Performance Analysis

## Overview

This project is a Python-based simulation framework designed to backtest and benchmark various artificial intelligence algorithms in two-player, zero-sum games (Tic-Tac-Toe and Reversi/Othello). It explores optimal decision-making, state space exploration, and the trade-offs between deterministic brute-force search and probabilistic heuristic evaluation.

By implementing algorithms like Minimax with Alpha-Beta Pruning and Monte Carlo Tree Search (MCTS), this project demonstrates practical applications of tree traversal, recursive optimization, and computational latency management.

## Core Algorithms Implemented

### 1. Deterministic Search: Minimax & Alpha-Beta Pruning

The standard Minimax algorithm explores the entire game tree to find the mathematically optimal move. However, for games with larger state spaces, this becomes computationally unfeasible. 
* **Complexity:** Standard Minimax evaluates $O(b^d)$ nodes, where $b$ is the branching factor and $d$ is the depth.
* **Optimization:** The Alpha-Beta pruning variant dynamically eliminates branches that cannot influence the final decision, significantly reducing the effective branching factor and allowing deeper search within the same computational time frame.

### 2. Heuristic Approximation: Depth-Limited Minimax
In Reversi, the state space is roughly $O(10^{28})$, making terminal search impossible. The depth-limited variant introduces a custom **heuristic evaluation function** to approximate the utility of non-terminal states. This mimics real-world scenarios where decisions must be made with incomplete information and strict time constraints, relying on proxies like piece mobility and corner control.

### 3. Probabilistic Search: Monte Carlo Tree Search (MCTS)

MCTS diverges from deterministic search by relying on randomized simulations (rollouts) to evaluate the potential of a given move. It elegantly balances **exploration** (trying new moves) and **exploitation** (focusing on moves with a high historical win rate) using the UCB1 formula:

$$UCB1 = \frac{w_i}{n_i} + c \sqrt{\frac{\ln N_i}{n_i}}$$

Where $w_i$ is the number of wins, $n_i$ is the node visits, $N_i$ is the parent visits, and $c$ is the exploration parameter.

## Simulation & Benchmarking Engine

The core of this project is the simulation engine (`main.py`), which allows for automated backtesting of different AI agents against one another over hundreds of trials. 

**Tracked Metrics:**
* **Win/Loss/Draw Rates:** Evaluates the strategic dominance of a given algorithm.
* **Computational Latency:** Tracks the exact execution time per move (`Average_Move_Time`), providing a quantitative measure of algorithmic efficiency and overhead.

### Simulation Results: Performance & Efficiency Benchmarks

The following data was gathered from 100-game simulations (20 for Reversi) running on a standard MacBook Air.

| Game Environment | Algorithm (Player 1) | Algorithm (Player 2) | Win / Loss / Draw | Avg Move Time (P1) | Avg Move Time (P2) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tic-Tac-Toe** | **Minimax (Pruning)** | Random | 100 / 0 / 0 | 0.0100s | 0.0000s |
| **Tic-Tac-Toe** | MCTS | Random | 96 / 4 / 0 | 0.0150s | 0.0000s |
| **Tic-Tac-Toe** | Minimax (Standard) | **Minimax (Pruning)** | 0 / 0 / 100 | 0.1865s | **0.0011s** |
| **Reversi** | **MCTS** | Limited Pruning | 12 / 4 / 4 | 13.8621s | **0.0655s** |

#### Key Algorithmic Insights:
1.  **Optimization Impact:** In the *Tic-Tac-Toe* benchmark, Alpha-Beta Pruning (Player 2) achieved the exact same theoretical outcome (Perfect Draw) as Standard Minimax (Player 1) but was approximately **170x faster** (0.0011s vs 0.1865s).
2.  **Trade-offs in Large State Spaces:** In *Reversi*, MCTS proved strategically superior (60% win rate) but required significantly higher computational resources (13.8s/move) compared to the heuristic-based Limited Pruning agent (0.06s/move).

## Project Architecture

The codebase is highly modular, separating the game environments from the decision-making agents:

* **`game.py`**: The abstract base class defining the environment constraints, state transitions, and utility functions.
* **Environments**: `tictactoe.py` and `reversi.py` implement the specific rules and state spaces.
* **Agents**: Individual modules (`mcts.py`, `minimax_pruning.py`, etc.) contain the isolated logic for each algorithmic strategy.
* **`main.py`**: The execution orchestrator and performance logger.

## Installation & Usage

### Prerequisites
* Python 3.x
* NumPy (Used for infinite value representations in pruning optimizations)

```bash
pip install numpy

```

### Running a Simulation

Execute the main script to enter the interactive simulation configuration:

```bash
python main.py

```

Follow the prompts to select the game environment, assign algorithms to Player 1 and Player 2, and define the number of  simulations to run. Performance statistics are generated upon completion.

## License

This project is open-source and available under the [MIT License](LICENSE.md).
