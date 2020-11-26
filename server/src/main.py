
import socket
from threading import Thread
import struct
import os

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1337        # Port to listen on (non-privileged ports are > 1023)

clients = []

packet_info = {
  # name
  0x7000: 30
}

def recv_message(s):
  data = b""
  try:
    data = s.recv(2)
  except ConnectionResetError:
    pass

  if not data:
    return

  id = struct.unpack("H", data)[0]
  msg_len = packet_info[id]
  
  return s.recv(msg_len)

def new_con_handler(conn, addr):
  while True:
    data = recv_message(conn)
    if not data:
      print(addr[0] + " has left me.")
      clients.remove(conn)
      break
    msg = data.decode('utf-8')
    print(addr[0] + ": " + msg)

def console(s):
  while True:
    user_input = input("$ ")
    if user_input[:5] ==  "clear":
      os.system("clear")
    else:
      for sock in clients:
        sock.sendall(struct.pack("H", 0x7000) + user_input.encode())

if __name__ == "__main__":
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((HOST, PORT))
  s.listen()

  Thread(target=console, args=(s,), daemon=True).start()

  while True:
    try:
      conn, addr = s.accept()
      clients.append(conn)
      conn.sendall(struct.pack("H", 0x7000) + b"Welcome to the server")
      Thread(target=new_con_handler, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
      break
    
  s.close()
