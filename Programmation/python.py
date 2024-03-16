import socket
import re
import math
import base64

def Retour_au_college():
    host = "challenge01.root-me.org"
    port = 52002 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        number = re.findall(r'\d+', s.recv(1024).decode())[1::]
        print(f"Numbers : {number}")
        result = str(round(math.sqrt(int(number[0])) * int(number[1]), 2)) + "\n"
        print(f"Anwser : {result}")
        s.send(result.encode())
        print(s.recv(1024).decode())

def Chaine_encode():
    host = "challenge01.root-me.org"
    port = 52023 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        b64 = re.findall(r"'(.*?)'", s.recv(1024).decode())[0]
        print(f"Numbers : {b64}")
        result = str(base64.b64decode(b64).decode()) + "\n"
        print(f"Anwser : {result}")
        s.send(result.encode())
        print(s.recv(1024).decode())


#Retour_au_college()
Chaine_encode()
