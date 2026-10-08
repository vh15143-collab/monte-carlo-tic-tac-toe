import math
import random


class Node:
    def __init__(self, board, player, parent=None, move=None):
        self.board = board[:]
        self.player = player
        self.parent = parent
        self.move = move

        self.children = []
        self.untried_moves = self.get_legal_moves()

        self.visits = 0
        self.wins = 0

    def get_legal_moves(self):
        return [
            i for i, cell in enumerate(self.board)
            if cell == ' '
        ]

    def winner(self):
        winning_lines = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8)
        ]

        for a, b, c in winning_lines:
            if (
                self.board[a] != ' ' and
                self.board[a] == self.board[b] == self.board[c]
            ):
                return self.board[a]

        return None

    def is_terminal(self):
        return (
            self.winner() is not None
            or len(self.get_legal_moves()) == 0
        )


def other_player(player):
    return 'O' if player == 'X' else 'X'


def apply_move(board, move, player):
    new_board = board[:]
    new_board[move] = player
    return new_board


def mcts(board, player, iterations=500):
    root_player = player

    root = Node(board, player)

    for _ in range(iterations):

        # -------------------------
        # 1. SELECTION
        # -------------------------
        node = root

        while not node.untried_moves and not node.is_terminal():
            node = best_uct_child(node)

        # -------------------------
        # 2. EXPANSION
        # -------------------------
        if node.untried_moves and not node.is_terminal():
            move = random.choice(node.untried_moves)
            node.untried_moves.remove(move)

            next_player = other_player(node.player)

            new_board = apply_move(
                node.board,
                move,
                node.player
            )

            child = Node(
                new_board,
                next_player,
                parent=node,
                move=move
            )

            node.children.append(child)
            node = child

        # -------------------------
        # 3. SIMULATION
        # -------------------------
        result = random_playout(node.board, node.player)

        # -------------------------
        # 4. BACKPROPAGATION
        # -------------------------
        while node is not None:
            node.visits += 1

            if result == root_player:
                node.wins += 1
            elif result == "draw":
                node.wins += 0.5

            node = node.parent

    best_child = max(
        root.children,
        key=lambda child: child.visits
    )

    return best_child.move, root


def best_uct_child(node):
    return max(
        node.children,
        key=lambda child: uct_value(child, node.visits)
    )


def uct_value(child, parent_visits):
    if child.visits == 0:
        return float('inf')

    exploitation = child.wins / child.visits

    exploration = math.sqrt(
        2 * math.log(parent_visits) / child.visits
    )

    return exploitation + exploration


def random_playout(board, player):
    simulation_board = board[:]
    current_player = player

    while True:

        winner = check_winner(simulation_board)

        if winner:
            return winner

        legal_moves = [
            i for i, cell in enumerate(simulation_board)
            if cell == ' '
        ]

        if not legal_moves:
            return "draw"

        move = random.choice(legal_moves)
        simulation_board[move] = current_player

        current_player = other_player(current_player)


def check_winner(board):
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 4, 6),
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
