import socket

HOST = '' # anyone can connect
PORT = 1337

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
