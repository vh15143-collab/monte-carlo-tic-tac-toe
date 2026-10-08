class TicTacToe:

    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def legal_moves(self):
        return [
            i for i, cell in enumerate(self.board)
            if cell == ' '
        ]

    def make_move(self, move):

        if move not in self.legal_moves():
            return False

        self.board[move] = self.current_player

        self.current_player = (
            'O'
            if self.current_player == 'X'
            else 'X'
        )

        return True

    def winner(self):

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
                self.board[a] != ' '
                and self.board[a] == self.board[b]
                and self.board[a] == self.board[c]
            ):
                return self.board[a]

        return None

    def is_draw(self):

        return (
            self.winner() is None
            and not self.legal_moves()
        )

    def is_terminal(self):

        return (
            self.winner() is not None
            or self.is_draw()
        )

    def display(self):

        print()

        for i in range(0, 9, 3):

            print(
                f" {self.board[i]} | "
                f"{self.board[i + 1]} | "
                f"{self.board[i + 2]} "
            )

            if i < 6:
                print("---+---+---")

        print()


if __name__ == "__main__":

    game = TicTacToe()

    print("Initial Tic-Tac-Toe Board:")
    game.display()
