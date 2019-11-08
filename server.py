#-----------------------------
#Import external Lib
#-----------------------------
import socket
import re
import os
import sys
import json
import jsonschema
import simplejson as json
from jsonschema import validate


#-----------------------------
#Import external file.Fonction
#-----------------------------
import jsonInject
import hash

#-----------------------------
#Param Socket SRV
#-----------------------------
HOST = '192.168.1.64'
PORT = 10010

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    #-----------------------------
    #Send Token, Init conn
    #-----------------------------
    token = hash.hash(10)
    conn.send(token.encode("Utf8"))
    msgClient = conn.recv(1024).decode("Utf8")
    while 1:
        #----------------------------------------
        #Check if receiveToken match with schema
        #----------------------------------------
        receiveToken = re.search("^[a-z0-9]+\.(user|admin)\.[a-z0-9]{32}$", msgClient)
        print(receiveToken)
        if receiveToken is not None:
            # --------------------------------------
            #Split token for generate and check sign
            # --------------------------------------
            importJson = 0
            contentToken = msgClient.split(".")
            confirmToken = hash.valideHash(contentToken[1], contentToken[2])
            conn.send(confirmToken[0].encode("Utf8"))
            code = confirmToken[1]
            if code == 1:
                print(confirmToken)
                # ----------------------------------------------------
                # If init token is true allow to receive one json data
                # ----------------------------------------------------
                while code == 1:
                    jsonFormat = 'Input Json Value EX:{"name":"John", "age":30, "city":"New York"}'
                    conn.send(jsonFormat.encode("Utf8"))
                    msgClient = conn.recv(1024).decode("Utf8")
                    # ----------------------------------------------------
                    # Check if json schema is ok
                    # ----------------------------------------------------
                    jsonContent = re.search('^{"name":"[a-zA-Z]+", "age":[0-9]+, "city":"[ a-zA-Z]+"}$', msgClient)
                    if jsonContent is not None:
                        jsonContent= json.loads(msgClient)
                        if jsonInject.checkJsonFormat(jsonContent) == True:
                            jsonInject.jsoninject(jsonContent)
                            CodeError = "Import ok"
                            conn.send(CodeError.encode("Utf8"))
                            code = 2
            else:
                print("Invalid User Role or Signature")
        else:
            confirmToken1 = "Invalid Token"
            conn.send(confirmToken1.encode("Utf8"))
        msgClient = conn.recv(1024).decode("Utf8")
        print("C>", msgClient)
        if msgClient.upper() == "FIN" or msgClient == "":
            break
