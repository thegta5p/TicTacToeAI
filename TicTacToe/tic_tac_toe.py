import random
import math

class TTT_cs170_judge:
    def __init__(self):
        self.board = []
        
    def create_board(self, n):
        for i in range(n):
            row = []
            for j in range(n):
                row.append('-')
            self.board.append(row)
            
    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()
            
    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        
        # Check columns
        for col in range(len(self.board)):
            if all([self.board[row][col] == player for row in range(len(self.board))]):
                return True
        
        # Check diagonals
        if all([self.board[i][i] == player for i in range(len(self.board))]):
            return True
        if all([self.board[i][len(self.board) - i - 1] == player for i in range(len(self.board))]):
            return True
        
        return False
    
    def is_board_full(self):
        return all([cell in ['X', 'O'] for row in self.board for cell in row])
    

class Player_1:
    def __init__(self, judge):
        self.board = judge.board
    
    def my_play(self):
        while True:
            row, col = map(int, input("Enter the row and column numbers separated by space: ").split())
            
            if 1 <= row <= len(self.board) and 1 <= col <= len(self.board[0]):
                self.board[row-1][col-1] = 'X'
                break
            else:
                print("Wrong coordination!")


class Player_2:
    def __init__(self, judge):
        self.judge = judge
        self.board = judge.board
    
    def minimax(self, board, depth, alpha, beta, isMaximizing):
        if self.judge.is_winner('O'):
            return 1
        elif self.judge.is_winner('X'):
            return -1
        elif self.judge.is_board_full():
            return 0
        
        if isMaximizing:
            best_score = -math.inf
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '-':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, alpha, beta, False)
                        board[i][j] = '-'
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = math.inf
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '-':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, alpha, beta, True)
                        board[i][j] = '-'
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score
        
    def my_play(self):
        best_score = -math.inf
        best_move = None
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == '-':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, -math.inf, math.inf, False)
                    self.board[i][j] = '-'
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            self.board[best_move[0]][best_move[1]] = 'O'
        
       
     # implment your code here
        
    

# Main Game Loop
def game_loop():
    n = 3  # Board size
    game = TTT_cs170_judge()
    game.create_board(n)
    player1 = Player_1(game)
    player2 = Player_2(game)
    starter = random.randint(0, 1)
    win = False
    if starter == 0:
        print("Player 1 starts.")
        game.display_board()
        while not win:
            player1.my_play()
            win = game.is_winner('X')
            game.display_board()
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
    else:
        print("Player 2 starts.")
        game.display_board()
        while not win:
            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
            
            player1.my_play()
            win = game.is_winner('X')
            game.display_board()
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

game_loop() # Uncomment this line to play the game, but it must be commented again when you are submitting the code
