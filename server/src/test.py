#!/usr/bin/env python3
import os
import socket
from threading import Thread
import struct
from main import recv_message

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1337      
      # The port used by the server

def recv_handler(socket):
    while True:
        data = recv_message(socket)
        if not data:
            print("Server is down.")
            break
        print("Server -> " + data.decode('utf-8'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    Thread(target=recv_handler, args=(s,), daemon=True).start()

    while True:
        user_input = input("$ ")
        if user_input[:5] == "clear":
            os.system("clear")
        elif not len(user_input):
            continue
        else:
            d = struct.pack("H", 0x7000) + user_input.encode()
            s.sendall(d)

