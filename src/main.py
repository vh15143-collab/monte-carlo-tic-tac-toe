import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mcts import mcts
from minimax import best_minimax_move


def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---+---+---")
    print()


def check_winner(board):
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in lines:
        if (
            board[a] != ' ' and
            board[a] == board[b] == board[c]
        ):
            return board[a]

    return None


def play_mcts_vs_minimax():
    board = [' '] * 9
    current_player = 'X'

    print("Monte Carlo Tic-Tac-Toe")
    print("MCTS (X) vs Minimax (O)")

    while True:

        print_board(board)

        winner = check_winner(board)

        if winner:
            print("Winner:", winner)
            break

        if ' ' not in board:
            print("Result: Draw")
            break

        if current_player == 'X':
            start = time.time()

            move, root = mcts(
                board,
                'X',
                iterations=500
            )

            elapsed = time.time() - start

            print(
                f"MCTS selected move: {move + 1}"
            )

            print(
                f"MCTS visits: {root.visits}"
            )

            print(
                f"MCTS time: {elapsed:.6f} seconds"
            )

        else:
            start = time.time()

            move = best_minimax_move(
                board,
                'O'
            )

            elapsed = time.time() - start

            print(
                f"Minimax selected move: {move + 1}"
            )

            print(
                f"Minimax time: {elapsed:.6f} seconds"
            )

        board[move] = current_player

        current_player = (
            'O'
            if current_player == 'X'
            else 'X'
        )


if __name__ == "__main__":
    play_mcts_vs_minimax()
