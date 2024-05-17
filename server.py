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
            data = conn.recv(1024 * 1024 * 1024)
            for i in data:
                shifted = ord(i) - 3
                msg += chr(shifted)
            print(f"\033[31;1;4m[ - ] Recieved: {msg}\033[0m")

            if b'sudo_end' == data:
                print("[ ! ] No Data received")
                print("[ - ] Closeing Connection")
                break

            msg = input("\033[31;1;4m[ * ] What to send?: \033[0m")
            for i in msg:
                shifted = ord(i) + 3
                msg += chr(shifted)
            msg.encode()
            print(f"[ + ] Sending: {msg}")
            conn.sendall(msg)


