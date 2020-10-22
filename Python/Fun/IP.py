import socket

hostname = socket.gethostname()
ip_adress = socket.gethostbyname(hostname)
print(f"hostname: {hostname}")
print(f"ip adress: {ip_adress}")