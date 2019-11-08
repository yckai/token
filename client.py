#-----------------------------
#Import external Lib
#-----------------------------
import socket
import io
import re

#-----------------------------
#Import external file.Fonction
#-----------------------------
import hash

#-----------------------------
#Param Socket SRV
#-----------------------------
HOST = '192.168.1.64'
PORT = 10010           # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msgServeur = s.recv(1024).decode("Utf8")

    while 1:
        # ----------------------------------------
        # Check if receiveToken match with schema
        # ----------------------------------------
        receiveToken = re.search("^[a-z0-9]+\.(user|admin)\.[a-z0-9]{32}$", msgServeur)
        # --------------------------------------
        # Split token for generate and check sign
        # --------------------------------------
        if receiveToken is not None:
            token = hash.hash(10)
            print(token)
            s.send(token.encode("Utf8"))
            msgServeur = s.recv(1024).decode("Utf8")
            print("S>", msgServeur)
            msgServeur = s.recv(1024).decode("Utf8")

        if msgServeur.upper() == "FIN" or msgServeur == "":
            break

        print("S>", msgServeur)
        msgClient = input("C> ")
        s.send(msgClient.encode("Utf8"))
        msgServeur = s.recv(1024).decode("Utf8")