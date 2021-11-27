import socket
from browser import FileBrowser
HEADER_LEN = 10
RESPONSE_LEN = 9999999999

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 8820))
while True:
    print("options:\n"
          "open\n"
          "show\n"
          "get abs path\n"
          "get file using abs path")
    choice = input("plz insert your choice\n")

    if choice == "show":
        my_socket.send(choice.encode())
        response = my_socket.recv(RESPONSE_LEN)
        print(f"server responds: {response.decode()}")

    if choice == "open":
        my_socket.send(choice.encode())
        folder_to_open = input("what would you like to open?\n")
        my_socket.send(folder_to_open.encode())
        response = my_socket.recv(RESPONSE_LEN)
        print(f"server responds: {response.decode()}")

    if choice == "get abs path":
        my_socket.send(choice.encode())
        folder_to_get_abs_path = input("what abs path would you like\n?")
        my_socket.send(folder_to_get_abs_path.encode())
        response = my_socket.recv(RESPONSE_LEN)
        print(f"server responds: {response.decode()}")

    if choice == "get file using abs path":
        my_socket.send(choice.encode())
        file_to_send = input("what file would you like\n?")
        my_socket.send(file_to_send.encode())

        f = open(file_to_send, "wb")
        tot_num_of_iteration = int.from_bytes(my_socket.recv(69), "big")
        print("the total number of the itaretion is " + str(tot_num_of_iteration))
        for i in range(tot_num_of_iteration):
            len_of_bytes_to_recive = int.from_bytes(my_socket.recv(4), "big")
            print("the len of bytes to recive is " + str(len_of_bytes_to_recive))
            l = my_socket.recv(len_of_bytes_to_recive)
            f.write(l)
        print(f"Im done receiving {file_to_send}")
        my_socket.close()
        f.close()


    if choice == "kill con":
        my_socket.send(choice.encode())
        break

my_socket.close()