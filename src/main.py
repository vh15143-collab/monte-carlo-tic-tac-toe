import time


def display_board(board):

    print()

    for i in range(0, 9, 3):

        print(
            f" {board[i]} | "
            f"{board[i + 1]} | "
            f"{board[i + 2]} "
        )

        if i < 6:
            print("---+---+---")

    print()


def check_winner(board):

    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_lines:

        if (
            board[a] != ' '
            and board[a] == board[b]
            and board[a] == board[c]
        ):
            return board[a]

    return None


def play_game():

    board = [' '] * 9

    current_player = 'X'

    move_number = 1

    print("Monte Carlo Tic-Tac-Toe")
    print("MCTS (X) vs Minimax (O)")

    print("\nInitial Board:")
    display_board(board)

    while True:

        # --------------------------------
        # MCTS plays X
        # --------------------------------

        if current_player == 'X':

            start_time = time.time()

            move, root = mcts(
                board,
                'X',
                iterations=500
            )

            end_time = time.time()

            print(
                f"Move {move_number}: "
                f"MCTS selected move: {move + 1}"
            )

            print(
                f"MCTS simulations: {root.visits}"
            )

            print(
                f"MCTS time: "
                f"{end_time - start_time:.6f} seconds"
            )

        # --------------------------------
        # Minimax plays O
        # --------------------------------

        else:

            start_time = time.time()

            move = best_minimax_move(
                board,
                'O'
            )

            end_time = time.time()

            print(
                f"Move {move_number}: "
                f"Minimax selected move: {move + 1}"
            )

            print(
                f"Minimax time: "
                f"{end_time - start_time:.6f} seconds"
            )

        # Apply selected move
        board[move] = current_player

        # Display board
        display_board(board)

        # Check winner
        winner = check_winner(board)

        if winner:

            print(
                "Winner:",
                winner
            )

            break

        # Check draw
        if ' ' not in board:

            print("Result: Draw")

            break

        # Change player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

        move_number += 1


if __name__ == "__main__":
    play_game()
