import socket
import pyfiglet
#################
G = '\033[2;32m'
Y = '\033[2;33m'
R = '\033[2;31m'
#################
a = input(G + "port from: ")
b = input(G + "port to: ")
c = input("url or ip: ")
logo = pyfiglet.figlet_format("Scanner")
print(G + logo)
print(f"Start Scaning On {c}")
for port in range(int(a), int(b)):
	try:
	  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	  sock.settimeout(0.40)
	  sock.connect((c, port))
	  print(Y + f"{port} [open] {socket.getservbyport(port)}")
	except:
		 print(R + f"{port} [close]")