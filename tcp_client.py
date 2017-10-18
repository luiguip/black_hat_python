import socket

target_host = 'www.google.com'
target_port = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((target_host, target_port))
client_socket.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
response = client_socket.recv(4096)
print(response)