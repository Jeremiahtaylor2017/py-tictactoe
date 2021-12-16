# Create Player class
class Player:
    def __init__(self, player):
        self.player = player


# Create Board with the majority of logic for game
class Board:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]  # Creates empty 2d array that is the board

    # Displays board
    def display_board(self):
        print('---------')
        for row in self.board:
            print('| ', end='')
            for col in row:
                print(f'{col} ', end='')
            print('|')
        print('---------')

    # Logic for placing the player on the board
    def move_player(self, player):
        try:
            coordinates = [int(i) for i in input("Enter coordinates for move: ").split()]
            x_coordinate = coordinates[0]
            y_coordinate = coordinates[1]
            if ((self.board[x_coordinate - 1][y_coordinate - 1] == 'X') or
                    (self.board[x_coordinate - 1][y_coordinate - 1] == 'O')):
                print("That space is occupied, please choose another one.")
                self.move_player(player)
            elif (x_coordinate < 1 or y_coordinate < 1) or (x_coordinate > 3 or y_coordinate > 3):
                print("Please only enter numbers between 1 and 3.")
                self.move_player(player)
            else:
                self.board[x_coordinate - 1][y_coordinate - 1] = player.player
        except (ValueError, IndexError):
            print("Please only enter numbers between 1 and 3.")
            self.move_player(player)

    # Checks the win condition for three across
    def check_across(self, player):
        for i in range(len(self.board)):
            if (self.board[i][0] == player.player and
                    self.board[i][1] == player.player and
                    self.board[i][2] == player.player):
                return True
        return False

    # Checks the win condition for three down
    def check_down(self, player):
        for i in range(len(self.board)):
            if (self.board[0][i] == player.player and
                    self.board[1][i] == player.player and
                    self.board[2][i] == player.player):
                return True
        return False

    # Checks the win condition for three diagonal
    def check_diagonal(self, player):
        if ((self.board[0][0] == player.player and
             self.board[1][1] == player.player and
             self.board[2][2] == player.player) or
                (self.board[0][2] == player.player and
                 self.board[1][1] == player.player and
                 self.board[2][0] == player.player)):
            return True
        return False

    # Methods for checking all three conditions to see if a player has won
    def has_won(self, player):
        if self.check_diagonal(player):
            return True
        elif self.check_across(player):
            return True
        elif self.check_down(player):
            return True
        return False

    # Methods to check for open spaces to help check for the status of the game
    def check_open_spaces(self):
        for row in self.board:
            for col in row:
                if col == ' ':
                    return True
        return False

    # Method to check that a player does not have more than 1 extra piece on the board. Should be impossible.
    def player_count_difference(self, p1, p2):
        p1_count = 0
        p2_count = 0

        for row in self.board:
            for col in row:
                if col == p1.player:
                    p1_count += 1
                elif col == p2.player:
                    p2_count += 1
        return (p1_count > p2_count + 1) or (p2_count > p1_count + 1)

    # Checks the game status and allows for the flow of the game to be smooth
    def game_status(self, p1, p2):
        if self.has_won(p1) and (self.has_won(p2)) or self.player_count_difference(p1, p2):
            return "Impossible game state"
        elif self.has_won(p1) and not self.has_won(p2):
            return "X Wins!!!"
        elif self.has_won(p2) and not self.has_won(p1):
            return "O Wins!!!"
        elif not self.has_won(p1) and not self.has_won(p2):
            if self.check_open_spaces():
                return "Game still in progress"
            else:
                return "Draw"
        else:
            return "Unknown"


if __name__ == '__main__':
    # Initialize all class instances to make game playable
    board = Board()
    player1 = Player('X')
    player2 = Player('O')
    player = player1

    print("""
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *   
    *                                                                                                               *
    *          * * * * *       * * * * *         * * *              * * * * *           *            * * *          *
    *              *               *           *      *                 *             *   *         *     *         *
    *              *               *           *                        *           *       *       *               *
    *              *               *           *                        *           * * * * *       *               *
    *              *               *           *                        *           *       *       *               *
    *              *               *           *      *                 *           *       *       *     *         *
    *              *           * * * * *         * * *                  *           *       *        * * *          *
    *                                                                                                               *
    *                                      * * * * *        * * *        * * * * *                                  *
    *                                          *           *     *       *                                          *
    *                                          *           *     *       *                                          *
    *                                          *           *     *       * * *                                      *
    *                                          *           *     *       *                                          *
    *                                          *           *     *       *                                          *
    *                                          *            * * *        * * * * *                                  *
    *                                                                                                               *
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
    """)

    # Explain the rules to the player
    print("""
        Welcome to Tic Tac Toe. The goal of the game is to get three in a row against the other player. That can be
      across, down, or diagonal. In order to place your player on the board, enter coordinates starting with "1 1" on
        the top left and "3 3" on the bottom right. Player 1 will be X and player 2 will be O. Are you ready? y/n.
    """)

    # Check for if the player is ready to play the game or not
    def yes_or_no():
        while True:
            answer = input()
            if answer.lower() == 'y':
                return True
            elif answer.lower() == 'n':
                return False
            print("Please enter y or n.")

    # Main logic for the game
    if yes_or_no():
        while True:
            board.display_board()
            result = board.game_status(player1, player2)

            if result == "Impossible game state" or result == "X Wins!!!" or result == "O Wins!!!" or result == "Draw":
                print(result)
                break

            board.move_player(player)

            if player == player1:
                player = player2
            else:
                player = player1
    else:
        print("Run program again when you are ready to play!")
