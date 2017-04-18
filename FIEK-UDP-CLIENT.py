from socket import *
import sys


print("Grupi AA1")
print("Projekti Rrjeta Kompjuterike")
print("UDP CLIENT LOADING...")
print("-----------------------\n")


serverAddress = "localhost"
serverPort = 9000

clientSocket = socket(AF_INET, SOCK_DGRAM)

print("Selekto metoden nga lista: IP , PING , TEMP")
sentence = input("KERKESA: ")

clientSocket.sendto(sentence.encode("utf-8"),(serverAddress,serverPort))
modifiedSentence = clientSocket.recv(1024)

print("Rezultati juaj: " + modifiedSentence.decode("utf-8"))


clientSocket.close()

