import socket
import sys
import ssl

# Define the client function
# This function is executed when the user chooses to act as a client (-c option)
def client():
    host = "bob1"  # Hostname of the server (Bob)
    port = 5006     # Port number to connect to

    # Create a socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Client socket created.')
    except socket.error as e:
        print(f'Error creating socket: {e}')
        sys.exit()

    # Resolve the IP address of the host
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Could not resolve hostname')
        sys.exit()

    # Connect to the server
    try:
        s.connect((remote_ip, port))
        print(f'Socket connected to {host} on IP: {remote_ip}')
    except Exception as e:
        print(f'Error connecting to server: {e}')
        sys.exit()

    # Initial message exchange
    try:
        s.send("chat_hello".encode())
        reply = s.recv(50)
        print(reply.decode())

        s.send("chat_STARTTLS".encode())
        reply = s.recv(50)
        print(reply.decode())

        # If server agrees to STARTTLS, wrap the socket with SSL/TLS
        if reply.decode() == "chat_STARTTLS_ACK":
            s = ssl.wrap_socket(s, 
                                keyfile="/root/alice-private-key.pem", 
                                certfile="/root/alice.crt", 
                                server_side=False,
                                ca_certs="/root/root.crt", 
                                cert_reqs=ssl.CERT_REQUIRED, 
                                ssl_version=ssl.PROTOCOL_TLS)
            print('TLS handshake completed.')
    except Exception as e:
        print(f'Error during communication: {e}')
        s.close()
        sys.exit()
