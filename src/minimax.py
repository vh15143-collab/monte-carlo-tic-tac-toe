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
            board[a] != ' ' and
            board[a] == board[b] == board[c]
        ):
            return board[a]

    return None


def minimax(board, maximizing_player='X'):
    winner = check_winner(board)

    if winner == maximizing_player:
        return 1

    opponent = 'O' if maximizing_player == 'X' else 'X'

    if winner == opponent:
        return -1

    legal_moves = [
        i for i, cell in enumerate(board)
        if cell == ' '
    ]

    if not legal_moves:
        return 0

    current_player = (
        'X'
        if board.count('X') == board.count('O')
        else 'O'
    )

    if current_player == maximizing_player:
        best_score = -float('inf')

        for move in legal_moves:
            board[move] = current_player
            score = minimax(board, maximizing_player)
            board[move] = ' '

            best_score = max(best_score, score)

        return best_score

    else:
        best_score = float('inf')

        for move in legal_moves:
            board[move] = current_player
            score = minimax(board, maximizing_player)
            board[move] = ' '

            best_score = min(best_score, score)

        return best_score


def best_minimax_move(board, player='X'):
    best_move = None
    best_score = -float('inf')

    for move in range(9):
        if board[move] == ' ':

            board[move] = player
            score = minimax(board, player)
            board[move] = ' '

            if score > best_score:
                best_score = score
                best_move = move

    return best_move
