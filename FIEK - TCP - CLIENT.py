import socket
import sys

print("Grupi AA1")
print("Projekti Rrjeta Kompjuterike")
print("TCP CLIENT LOADING...")
print("-----------------------\n")


serverName = 'localhost' # shtoni ip-ne tuaj
serverPort = 9000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Selekto metoden nga lista: IP , PING , TEMP")
sentence = input("KERKESA: ")

clientSocket.send(sentence.encode('ASCII'))
modifiedSentence = clientSocket.recv(1024)
condition = modifiedSentence.decode('ASCII')
print("Rezultati juaj: " + condition)


clientSocket.close()