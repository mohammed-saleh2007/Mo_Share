import socket

HOST = input("HOST?: ")
PORT = int(input("PORT?: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"[ ! ] Connected to: {HOST}:{PORT}")
    while True:
        user_input = input("[ * ] > ")
        msg = user_input.encode()
        s.sendall(msg)

        if user_input == "break":
            print(" [ ! ] Sending termination signal!")
            print("\ngoodbye :)\n")
            break

        print("[ * ] Receiving ...")
        data = s.recv(1024 * 1024 * 1024)
        print(f"\033[31;1;4m[ - ] server: {data!r}\033[0m")
