class Move:
    def __init__(self, x, y, sign):
        self.x = x
        self.y = y
        self.sign = sign


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def get_move(self):
        while True:
            try:
                x, y = map(int, input(f"{self.name} ({self.sign}), podaj swój ruch (wiersz i kolumna): ").split())
                return Move(x, y, self.sign)
            except ValueError:
                print("Nieprawidłowe dane wejściowe. Proszę wpisać dwie liczby całkowite oddzielone spacją.")


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def __str__(self):
        state = "\n"
        for row in self.board:
            state += "|".join(row) + "\n"
            state += "-+-+-\n"
        return state[:-5]

    def get_state(self):
        print(self.__str__())

    def get_field(self, x, y):
        return self.board[x][y]

    def set_field(self, move):
        self.board[move.x][move.y] = move.sign


class Game:
    def __init__(self):
        self.board = Board()

    def play(self, player_one, player_two):
        current_player = player_one
        for _ in range(9):
            self.board.get_state()
            move = current_player.get_move()
            self.board.set_field(move)

            if self.game_over(current_player):
                self.board.get_state()
                print(f"{current_player.name} wygrywa!")
                return 1 if current_player == player_one else -1

            current_player = player_two if current_player == player_one else player_one

        self.board.get_state()
        print("Remis!")
        return 0

    def game_over(self, player):
        sign = player.sign
        b = self.board.board

        for i in range(3):
            if all(b[i][j] == sign for j in range(3)) or all(b[j][i] == sign for j in range(3)):
                return True

        if b[0][0] == b[1][1] == b[2][2] == sign or b[0][2] == b[1][1] == b[2][0] == sign:
            return True

        return False



player_one = Player("Player One", "O")
player_two = Player("Player Two", "X")
game = Game()
game.play(player_one, player_two)
