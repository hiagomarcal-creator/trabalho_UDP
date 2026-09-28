from socket import *

serverName = '127.0.0.1'
serverPort = 1217
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Digite uma frase em minúsculas: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()