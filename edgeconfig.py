import socket
from Database import Database

db = Database()

def main(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip, port))
	sock.listen()

	print(f'Edge is runnin on {ip}:{port}')

	while True:
		balancer, _ = sock.accept()
		request = balancer.recv(2048).decode('utf-8').split('|')
		print(request)
		auth = db.auth(request[2], request[3])
		if len(auth) > 0:
			response = 'Deu bom'
		else:
			response = 'Não autenticado'	
		balancer.sendall(response.encode())
		balancer.close()