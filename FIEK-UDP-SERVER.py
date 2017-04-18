import socket
import random
import datetime
from time import gmtime, strftime

print("UP-FIEK")
print("Rrjeta Kompjuterike")
print("UDP Server")
print("-----------------------\n")

serverPort=9000

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('localhost',serverPort))

print ("Serveri eshte i gatshem per pranimin e kerkesave...")

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

while True:

    message, clientAddress = serverSocket.recvfrom(1024)
    message = message.decode("utf-8")
    capitalizedSentence = message.upper()
    textRecieved = capitalizedSentence
    condition = capitalizedSentence.split(' ')

    if len(condition) == 1:
        condition1 = capitalizedSentence.split(' ')[0]
    elif len(condition) == 2:
        condition1 = capitalizedSentence.split(' ')[0]
        condition2 = capitalizedSentence.split(' ')[1]

    elif len(condition) == 3:
        condition1 = capitalizedSentence.split(' ')[0]
        condition2 = capitalizedSentence.split(' ')[1]
        condition3 = capitalizedSentence.split(' ')[2]

    rez = 0.0

    if condition1 == "KONVERTO":
        if condition2 == "CELSIUSTOKELVIN":
            int(condition3)
            rez = CelsiustoKelvin(condition3)
            rez = str(rez)
            serverSocket.sendto(rez.encode("utf-8"),clientAddress)

        elif condition2 == "CELSIUSTOFARENTHEIT":
            int(condition3)
            rez = CelsiustoFahrenheit(condition3)
            rez = str(rez)
            serverSocket.sendto(rez.encode("utf-8"),clientAddress)
        elif condition2 == "KELVINTOCELSIUS":
            int(condition3)
            rez = KelvintoCelsius(condition3)
            rez = str(rez)
            serverSocket.sendto(rez.encode("utf-8"),clientAddress)
        elif condition2 == "KELVINTOFARENTHEIT":
            int(condition3)
            rez = KelvintoFahrenheit(condition3)
            rez = str(rez)
            serverSocket.sendto(rez.encode("utf-8"),clientAddress)
        elif condition2 == "FARENTHEITTOCELSIUS":
            int(condition3)
            rez = FarentheitToCelsius(condition3)
            rez = str(rez)
            serverSocket.sendto(rez.encode("utf-8"),clientAddress)
        elif condition2 == "FARENTHEITTOKELVIN":
            int(condition3)
            rez = FahrentheiottoKelvin(condition3)
            rez = str(rez)
            serverSocket.sendto(rez.encode("utf-8"),clientAddress)
        elif condition2 == "POUNDTOKILOGRAM":
            int(condition3)
            rez = PoundToKg(condition3)
            rez = str(rez)
            serverSocket.sendto(rez.encode("utf-8"),clientAddress)
        elif condition2 == "KILOGRAMTOPOUND":
            int(condition3)
            rez = KgToPound(condition3)
            rez = str(rez)
            serverSocket.sendto(rez.encode("utf-8"),clientAddress)
    elif condition1 == "KENO":
        array = []
        for i in range(0, 20):
            array.append(random.randint(1, 80))
        array.sort()
        keno = str(array)[1:-1]
        serverSocket.sendto(keno.encode("utf-8"),clientAddress)
    elif condition1 == "ZANORET":

        nrZan = zanore(textRecieved)
        nrZan = int(nrZan) - 3
        nrZan = str(nrZan)
        serverSocket.sendto(nrZan.encode("utf-8"),clientAddress)
    elif condition1 == "TIME":
        now = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        serverSocket.sendto(now.encode("utf-8"),clientAddress)
    elif condition1 == "IP":
        ip = serverSocket.getpeername()
        ip = str(ip)
        serverSocket.sendto(ip.encode("utf-8"),clientAddress)
    elif condition1 == "HOST":
        host = serverSocket.gethostname()
        host = str(host)
        serverSocket.sendto(host.encode("utf-8"),clientAddress)
    elif condition1 == "PORT":
        port = serverSocket.getsockname()
        port = str(port)
        serverSocket.sendto(port.encode("utf-8"),clientAddress)
    elif condition1 == "FAKTORIEL":
        num = int(condition2)

        factorial = 1

        if num < 0:
            rezfakt = ("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            rezfakt = ("The factorial of 0 is 1")
        else:
            for i in range(1, num + 1):
                factorial = factorial * i
            rezfakt = ("The factorial of", num, "is", factorial)
        rezfakt = str(rezfakt)
        serverSocket.sendto(rezfakt.encode("utf-8"),clientAddress)
    elif condition1 == "JASMIN1":
        pi = 22 / 7
        radian = float(condition2)
        grad = radian * (180 / pi)
        grad = str(grad)
        serverSocket.sendto(grad.encode("utf-8"),clientAddress)

    elif condition1 == "ARDITA1":
        s = textRecieved
        d = l = 0
        for c in s:
            if c.isdigit():
                d = d + 1
            elif c.isalpha():
                l = l + 1
            else:
                pass

        rezard = ("Shkronja: ",l," Numra: ",d)
        rezard = str(rezard)
        serverSocket.sendto(rezard.encode("utf-8"),clientAddress)
    elif condition1 == "REDZEP1":
        baza = int(condition2)
        lartesia = int(condition3)
        siperfaqe = baza * lartesia
        siperfaqe = str(siperfaqe)
        serverSocket.sendto(siperfaqe.encode("utf-8") , clientAddress)
    elif condition1 == "JASMIN2":
        num1 = int(condition1)
        num2 = int(condition2)
        if (num1 > num2):
            largest = num1
        elif (num2 > num1):
            largest = num2

        largest = str(largest)
        serverSocket.sendto(largest.encode("utf-8"), clientAddress)
    elif condition1 == "REDZEP2":
        gb = int(condition2)
        mb = gb / 1024
        gb = str(gb)
        serverSocket.sendto(gb.encode("utf-8"), clientAddress)

    elif condition1 == "ANITA1":
        numpertvsh = int(condition2)
        numrez = numpertvsh / 0.18
        numrez = str(numrez)
        serverSocket.sendto(numrez.encode("utf-8"), clientAddress)
    elif condition1 == "ANITA2":
        age = int(condition2)
        if age < 18 :
            rezanita = "You are not allowed to drive"
        else:
            rezanita = "You are allowed to drive"
        serverSocket.sendto(rezanita.encode("utf-8"), clientAddress)
    elif condition1 == "ARDITA2":
        numripeq = int(condition2)
        numridy = int(condition3)
        numricalc = (numripeq * numridy) / 100
        numricalc = str(numricalc)
        serverSocket.sendto(numricalc.encode("utf-8"), clientAddress)
    elif condition1 == "PRINT":
        serverSocket.send(condition2.encode("utf-8"), clientAddress)
    else:
        err = "Metoda nuk perkrahet nga serveri yne"
        serverSocket.sendto(err.encode("utf-8"),clientAddress)


print("Rezultati eshte derguar nga serveri")
serverSocket.close()