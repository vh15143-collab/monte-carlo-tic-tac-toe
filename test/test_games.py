def test_tictactoe():

    game = TicTacToe()

    assert len(game.board) == 9
    assert game.winner() is None
    assert game.is_draw() is False

    print("Tic-Tac-Toe test passed")


def test_mcts():

    board = [' '] * 9

    move, root = mcts(
        board,
        'X',
        iterations=500
    )

    assert move is not None
    assert 0 <= move <= 8
    assert root.visits == 500

    print("MCTS test passed")
    print("MCTS selected move:", move + 1)
    print("Total simulations:", root.visits)


def test_minimax():

    board = [
        'X', 'X', ' ',
        'O', ' ', ' ',
        ' ', ' ', ' '
    ]

    move = best_minimax_move(
        board,
        'O'
    )

    assert move is not None
    assert 0 <= move <= 8

    print("Minimax test passed")
    print("Minimax selected move:", move + 1)


if __name__ == "__main__":

    print("Running Tic-Tac-Toe Tests")
    print("-------------------------")

    test_tictactoe()
    test_mcts()
    test_minimax()

    print("-------------------------")
    print("All tests passed successfully!")
