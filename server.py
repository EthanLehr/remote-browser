import math
import socket
from datetime import datetime
import os
from browser import FileBrowser

HOST = "0.0.0.0"  # Symbolic name meaning all available interfaces
PORT = 8820  # Arbitrary non-privileged port
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)

conn, addr = socket.accept()
print('Connected by', addr)
broswer = FileBrowser()


def send_file(path_to_file):
    file = open(path_to_file, 'rb')
    size = os.path.getsize(path_to_file)
    num_of_full_iteration = size // 1024  # floor divition
    size_of_part_iteration = size % 1024
    b = file.read(1024)
    tot_num_of_iteration = math.ceil(size / 1024)
    conn.sendall((tot_num_of_iteration).to_bytes(69, byteorder='big'))
    for i in range(num_of_full_iteration):
        conn.sendall((1024).to_bytes(4, byteorder='big'))
        conn.sendall(b)
        b = file.read(1024)
    conn.sendall((size_of_part_iteration).to_bytes(4, byteorder='big'))
    conn.sendall(b)
    file.close()


while True:
    data = conn.recv(50)
    if data.decode() == "show":
        dir_items_as_str = broswer.show_directory()
        conn.sendall(dir_items_as_str.encode())
    if data.decode() == "open":
        folder_to_open = conn.recv(1000).decode()
        dir_items_str = broswer.open_directory(folder_to_open)
        conn.sendall(dir_items_str.encode())
    if data.decode() == "get abs path":
        path_to_get = conn.recv(1000).decode()
        conn.sendall(broswer.get_file_path(path_to_get).encode())
    if data.decode() == "get file using abs path":
        path_to_file = conn.recv(1000).decode()
        send_file(path_to_file)

    if data.decode() == "kill con":
        break

conn.close()

