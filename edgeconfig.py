import socket

def main(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip, port))
	sock.listen()

	print(f'Edge is runnin on {ip}:{port}')

	while True:
		balancer, _ = sock.accept()
		request = balancer.recv(2048)
		print(request)
		response = 'Deu bom'
		balancer.sendall(response.encode())
		balancer.close()