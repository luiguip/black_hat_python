import socket

target_host = '127.0.0.1'
target_port = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b'AAABBBCCC', (target_host,target_port))
data, addr = client_socket.recvfrom(1024)
print(data)