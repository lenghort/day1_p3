import socket

HOST = '127.0.0.1'
PORT = 21002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

conn, addr = s.accept()
with conn:
    print('Connection accepted from ', addr)

    while True:
        message = input("Enter a message: ")
        s.send((message+"\n").encode())

        message_received = ""
        while True:
            data = s.recv(32)
            if data:
                print('Received data chunk from server: ', repr(data))
                message_received += data.decode()
                if message_received.endswith("\n"):
                    print("End of message received")
                    break
            else:
                print("Connection lost!")
                break

        if message_received:
            print("Received message: ", message_received)
            conn.send(("Server summarized: " + message_received[:10] + "\n").encode())
        else:
            break

print("Client finished")