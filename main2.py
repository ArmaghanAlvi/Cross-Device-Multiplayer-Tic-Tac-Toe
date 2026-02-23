import socket #A network socket is the communication link between two programs in a network
                #Includes a network protocol (ex. TCP/UDP), IP address, and port number
import threading #We need two threads, one for user input, one for processing the opponenet's actions

class TicTacToe:

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.you = "X"
        self.opponent = "O"
        self.winner = "None"
        self.gameOver = False
        self.counter = 0

    #Function for the host 
    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket with intenrnet communication, TCP socket - maintains connection
        server.bind((host, port)) #Binding host socket to a port
        server.listen(1) #Allows server to accept connections (backlog 1 - aka, can have 1 pending connection in the queue)

        client, addr = server.accept() #Allows it to accept a connection

        self.you = 'X'
        self.opponent = 'O'
        threading.Thread(target = self.handle_connection, args = (client,)).start() #Creates and starts new thread
        server.close() #Closes once one connection is made sense its purpose is to connect a client and a host for a game, not host multiple games

    #Function for the client to connect to host
    def connect_to_game(self, host, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port)) #Allows remote socket to connect to server

        self.you = 'O'
        self.opponent = 'X'
        threading.Thread(target = self.handle_connection, args = (client,)).start()

    #Turn handling
    def handle_connection(self, client):
        while not self.gameOver:
            #Your turn
            if self.turn == self.you:
                move = input("Enter a move (row,col): ")
                if self.check_valid_move(move.split(',')):
                    client.send(move.encode('utf-8')) #turns the string into bytes and sends it to the client
                    self.apply_move(move.split(','), self.you)
                    self.turn = self.opponent
                else: 
                    print("Invalid move!")
            #Recieving opponent's move
            else:
                data = client.recv(1024) #Recieves data from the client 
                if not data:
                    break
                else:
                    self.apply_move(data.decode('utf-8').split(','), self.opponent) #turns recieved bytes into string, splits to use in apply_move for the opponenet
                    self.turn = self.you

        client.close() #closes socket

    #Function for applying moves to the board
    def apply_move(self, move, player):
        if self.gameOver:
            return
        
        self.counter += 1
        self.board[int(move[0])][int(move[1])] = player
        self.print_board()
        
        if self.check_if_won():
            if self.winner == self.you:
                print("You win!")
                exit()
            elif self.winner == self.opponent:
                print("You lose!")
                exit()
        else:
            if self.counter == 9:
                print("It's a tie!")
                exit()

    def check_valid_move(self, move):
        return self.board[int(move[0])][int(move[1])] == " "
    
    def check_if_won(self):
        #Checking for row wins
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ": 
                self.winner = self.board[row][0]
                self.game_over = True
                return True
            
        #Checking for col wins
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ": 
                self.winner = self.board[0][col]
                self.game_over = True
                return True

        #Checking for diagonal wins
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner = self.board[0][0]
            self.game_over = True
            return True

        if self.board[2][0] == self.board[1][1] == self.board[0][2] != " ":
            self.winner = self.board[2][0]
            self.game_over = True
            return True
        
        return False

    def print_board(self):
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("-----------")
    
#Executing the code
game = TicTacToe()
game.connect_to_game("localhost", 9999) #We're doing localhost since we're testing on the same device
    













#TO-DO:
#Figure out how to connect over internet
#Make UI