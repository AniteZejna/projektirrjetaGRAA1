from socket import *
import random
import datetime
from time import gmtime, strftime


print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("TCP Server")
print("-----------------------\n")

serverPort = 9000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)

print("Serveri eshte gati per pranim te dhenave...")


# konvertori
def FarentheitToCelsius(f):
    return float((int(f) - 32) / 1.8)


def CelsiustoFahrenheit(c):
    return float(int(c) - 1.8 + 32)


def CelsiustoKelvin(c):
    return float(int(c) + 273.15)


def KelvintoCelsius(k):
    return float(int(k) - 273.15)


def FahrentheiottoKelvin(f):
    return float((int(f) + 459.67) * 5 / 9)


def KelvintoFahrenheit(k):
    return float(int(k) * (9 / 5) - 459.67)


def KgToPound(kg):
    return float(int(kg) / 0.45)


def PoundToKg(lb):
    return float(int(lb) * 0.45)



#zanoret
def zanore(string):
    zanoret = 0
    for i in string:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'Y'):
            zanoret = zanoret + 1
    return int(zanoret)

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    textRecieved = capitalizedSentence.decode()
    condition = capitalizedSentence.decode().split(' ')

    if len(condition) == 1:
        condition1 = capitalizedSentence.decode().split(' ')[0]
    elif len(condition) == 2:
        condition1 = capitalizedSentence.decode().split(' ')[0]
        condition2 = capitalizedSentence.decode().split(' ')[1]

    elif len(condition) == 3:
        condition1 = capitalizedSentence.decode().split(' ')[0]
        condition2 = capitalizedSentence.decode().split(' ')[1]
        condition3 = capitalizedSentence.decode().split(' ')[2]

    rez = 0.0

    if condition1 == "KONVERTO":
        if condition2 == "CELSIUSTOKELVIN":
            int(condition3)
            rez = CelsiustoKelvin(condition3)
            rez = str(rez)
            connectionSocket.send(rez.encode('ASCII'))
        elif condition2 == "CELSIUSTOFARENTHEIT":
            int(condition3)
            rez = CelsiustoFahrenheit(condition3)
            rez = str(rez)
            connectionSocket.send(rez.encode('ASCII'))
        elif condition2 == "KELVINTOCELSIUS":
            int(condition3)
            rez = KelvintoCelsius(condition3)
            rez = str(rez)
            connectionSocket.send(rez.encode('ASCII'))
        elif condition2 == "KELVINTOFARENTHEIT":
            int(condition3)
            rez = KelvintoFahrenheit(condition3)
            rez = str(rez)
            connectionSocket.send(rez.encode('ASCII'))
        elif condition2 == "FARENTHEITTOCELSIUS":
            int(condition3)
            rez = FarentheitToCelsius(condition3)
            rez = str(rez)
            connectionSocket.send(rez.encode('ASCII'))
        elif condition2 == "FARENTHEITTOKELVIN":
            int(condition3)
            rez = FahrentheiottoKelvin(condition3)
            rez = str(rez)
            connectionSocket.send(rez.encode('ASCII'))
        elif condition2 == "POUNDTOKILOGRAM":
            int(condition3)
            rez = PoundToKg(condition3)
            rez = str(rez)
            connectionSocket.send(rez.encode('ASCII'))
        elif condition2 == "KILOGRAMTOPOUND":
            int(condition3)
            rez = KgToPound(condition3)
            rez = str(rez)
            connectionSocket.send(rez.encode('ASCII'))
    elif condition1 == "KENO":
        array = []
        for i in range(0, 20):
            array.append(random.randint(1, 80))
        array.sort()
        keno = str(array)[1:-1]
        connectionSocket.send(keno.encode('ASCII'))
    elif condition1 == "ZANORET":

        nrZan = zanore(textRecieved)
        nrZan = int(nrZan) - 3
        nrZan = str(nrZan)
        connectionSocket.send(nrZan.encode('ASCII'))
    elif condition1 == "TIME":
        now = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        connectionSocket.send(now.encode('ASCII'))
    elif condition1 == "IP":
        ip = serverSocket.getpeername()
        ip = str(ip)
        connectionSocket.send(ip.encode('ASCII'))
    elif condition1 == "HOST":
        host = serverSocket.gethostname()
        host = str(host)
        connectionSocket.send(host.encode('ASCII'))
    elif condition1 == "PORT":
        port = serverSocket.getsockname()
        port = str(port)
        connectionSocket.send(port.encode('ASCII'))
    else:
        err = "Metoda nuk perkrahet nga serveri yne"
        connectionSocket.send(err.encode('ASCII'))


    print("Rezultati eshte derguar nga serveri")

    connectionSocket.close()