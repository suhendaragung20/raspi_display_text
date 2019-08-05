import socket



# Get host and port
host = "192.168.43.150"
port = 60000

# Create new server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)

sock_client, address_client = sock.accept()

print("Connected with " + str(address_client))

text_display = ""

while True:

    try:
        data = sock_client.recv(32)
    except:
        print("Client " + str(address_client) + " has disconnected")
        break
    if data != "":
        print(str(data.decode("utf-8")))
        text_display = str(data.decode("utf-8"))
        with open('display_text.txt', 'w') as f:
            f.write("%s\n" % text_display)