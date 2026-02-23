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
                    self.apply_move(move.split(','), self.you)
                    self.turn = self.opponent
                    client.send(move.encode('utf-8')) #turns the string into bytes and sends it to the client
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



    













#TO-DO:
#Figure out how to connect over internet
#Make UI