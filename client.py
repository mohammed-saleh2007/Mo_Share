import socket

HOST = input("HOST?: ")
PORT = int(input("PORT?: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        user_input = input("\033[31;1;4m[ * ] What to send?: \033[0m")
        user_input.encode()
        print(f"[ ! ] Connected to: {HOST}:{PORT}")
        s.sendall(user_input)
        print("[ + ] Sending...")
        print("[ * ] Receiving data ...")
        data = s.recv(1024 * 1024 * 1024)
        print("[ + ] Receiving...")
        print(f"\033[31;1;4m[ - ] Recieved: {msg!r}\033[0m")
