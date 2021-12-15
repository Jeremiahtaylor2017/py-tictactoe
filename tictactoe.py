class Player:
    def __init__(self, player):
        self.player = player


class Board:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]

    def display_board(self):
        print('---------')
        for row in self.board:
            print('| ', end='')
            for col in row:
                print(f'{col} ', end='')
            print('|')
        print('---------')

    def move_player(self, player):
        try:
            coordinates = [int(i) for i in input("Enter coordinates for move: ").split()]
            xCoordinate = coordinates[0]
            yCoordinate = coordinates[1]
            if ((self.board[xCoordinate - 1][yCoordinate - 1] == 'X') or
                    (self.board[xCoordinate - 1][yCoordinate - 1] == 'O')):
                print("That space is occupied, please choose another one.")
                self.move_player(player)
            elif (xCoordinate < 1 or yCoordinate < 1) or (xCoordinate > 3 or yCoordinate > 3):
                print("Please only enter numbers between 1 and 3.")
                self.move_player(player)
            else:
                self.board[xCoordinate - 1][yCoordinate - 1] = player.player
        except (ValueError, IndexError):
            print("Please only enter numbers between 1 and 3.")
            self.move_player(player)

    def check_across(self, player):
        for i in range(len(self.board)):
            if (self.board[i][0] == player.player and
                    self.board[i][1] == player.player and
                    self.board[i][2] == player.player):
                return True
        return False

    def check_down(self, player):
        for i in range(len(self.board)):
            if (self.board[0][i] == player.player and
                    self.board[1][i] == player.player and
                    self.board[2][i] == player.player):
                return True
        return False

    def check_diagonal(self, player):
        if ((self.board[0][0] == player.player and
             self.board[1][1] == player.player and
             self.board[2][2] == player.player) or
                (self.board[0][2] == player.player and
                 self.board[1][1] == player.player and
                 self.board[2][0] == player.player)):
            return True
        return False

    def has_won(self, player):
        if self.check_diagonal(player):
            return True
        elif self.check_across(player):
            return True
        elif self.check_down(player):
            return True
        return False


if __name__ == '__main__':
    board = Board()
    player1 = Player('X')
    player2 = Player('O')
    player = player1

    while True:
        board.display_board()
        board.move_player(player)

        if board.has_won(player):
            board.display_board()
            print(f'{player.player} wins!!!')
            break

        if player == player1:
            player = player2
        else:
            player = player1
