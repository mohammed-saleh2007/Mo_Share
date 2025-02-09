import socket

HOST = "0.0.0.0"
PORT = 8080 #int(input("Port?: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[ * ] Listening...")
    conn, addr = s.accept()
    with conn:
        print(f"[ ! ] Connected by {addr}")
        while True: 
            print("[ + ] Receiving data ...")
            msg = conn.recv(1024 * 1024 * 1024)
            print(f"\033[31;1;4m[ - ] Recieved: {msg}\033[0m")
            if msg == "break":
		print("[ ! ] Terminate signal recived!")
		break
            msg = input("\033[31;1;4m[ * ] What to send?: \033[0m")
            print(f"[ + ] Sending: {msg}")
            conn.sendall(msg)


