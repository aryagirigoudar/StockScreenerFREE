import socket


HOST = "192.168.186.23"  # The server's hostname or IP address
PORT = 65434  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    a='y'
    while (a != "n"):
        myData = str(input("Enter message:  "))
        s.sendall(myData.encode('utf-8'))
        data = s.recv(1024)
        if not data:
            break
        print(f"Received {data!r}")
        a=str(input("Enter n if you want to close: "))
        if (a == 'n'):
            break




