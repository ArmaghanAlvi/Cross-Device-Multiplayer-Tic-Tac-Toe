import socket
import threading #We need two threads, one for user input, one for processing the opponenet's actions

class TicTacToe:

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.host = "X"
        self.opponent = "O"
        self.winner = "None"
        self.gameOver = False
        self.counter = 0

    #Function for the host 
    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket with intenrnet communication, TCP socket - maintains connection
        server.bind((host, port)) #Binding host socket
        server.listen(1) #Allows server to accept connections (backlog 1 - aka, can have 1 pending connection in the queue)

        client, addr = server.accept() #Allows it to accept a connection

        self.host = "X"
        self.opponent = "O"
        threading.Thread(target = self.handle_connection, args = (client,)).start()
        server.close() #Closes once one connection is made sense its purpose is to connect a client and a host for a game, not host multiple games

    













#TO-DO:
#Figure out how to connect over internet
#Make UI