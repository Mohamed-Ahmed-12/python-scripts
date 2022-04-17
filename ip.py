import socket 
host = input("Enter Host Name: ")
ip = socket.gethostbyname(host)
print("IP: ",ip)