import socket
import re
import math

def Retour_au_college():
    host = "challenge01.root-me.org"
    port = 52002 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        number = re.findall(r'\d+', s.recv(1024).decode())[1::]
        print(f"Numbers : {number}")
        result = str(round(math.sqrt(int(number[0])) * int(number[1]), 2)) +"\n"
        print(f"Anwser : {result}")
        s.send(result.encode())
        print(s.recv(1024).decode())

Retour_au_college()
