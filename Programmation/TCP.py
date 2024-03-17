import socket
import re
import math
import base64
import subprocess

def generic_socket_connection(host, port, process_function):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = s.recv(1024).decode()
        while "flag" not in data:
            print(f"Data received: {data}")
            result = process_function(data) + "\n"
            print(f"Answer: {result}")
            s.send(result.encode())
            data = s.recv(1024).decode()
        print(f"Data received: {data}")

def retour_au_college(data):
    number = re.findall(r'\d+', data)[1::]
    return str(round(math.sqrt(int(number[0])) * int(number[1]), 2))

def chaine_encode(data):
    b64 = re.findall(r"'(.*?)'", data)[0]
    return base64.b64decode(b64).decode()

def la_roue_romaine(data):
    msg = re.findall(r"'(.*?)'", data)[0]
    result = ""
    if msg:
        for char in msg:
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                if 65 <= ord(char) <= 90:
                    # capitlized case
                    if ord(char) + 13 > 90:
                        char = chr(ord(char) + 13 - 90 + 65 - 1)
                    else:
                        char = chr(ord(char) + 13)
                else:
                    # lowercase
                    if ord(char) + 13 > 122:
                        char = chr(ord(char) + 13 - 122 + 97 - 1)
                    else:
                        char = chr(ord(char) + 13)
            else:
                pass
            result += char
    return result

def uncompress_me(data):
    b64 = re.findall(r"'(.*?)'", data)[0]
    command = f'echo "{b64}" | base64 -d | pigz -d -z'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        print("Fuck, here we go again")

Retour_au_college = lambda: generic_socket_connection(host, 52002, retour_au_college)
Chaine_encode = lambda: generic_socket_connection(host, 52023, chaine_encode)
La_roue_romaine = lambda: generic_socket_connection(host, 52021, la_roue_romaine)
Uncompress_me = lambda: generic_socket_connection(host, 52022, uncompress_me)

if __name__ == '__main__':
    host = "challenge01.root-me.org"
    Retour_au_college()
    Chaine_encode()
    La_roue_romaine()
    Uncompress_me()