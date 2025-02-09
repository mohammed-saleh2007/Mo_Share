import socket

HOST = "0.0.0.0"
PORT = int(input("Port?: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[ * ] Listening...")
    conn, addr = s.accept()
    print(f"[ ! ] Connected by {addr}")
    with conn:
        while True: 
            print("[ + ] Receiving ...")
            client_msg = conn.recv(1024 * 1024 * 1024)
            print(f"[ - ] Client: {client_msg}")
            if client_msg.decode() == "break":
                print("[ ! ] Terminate signal recived!")
                break
            msg = input("[ * ] >  ")
            msg.encode() 
            conn.sendall(msg.encode())
            print(f"[ + ] server: {msg}")


