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
		request = balancer.recv(2048)
		split_request = request.decode('utf-8').split('|')
		auth = db.auth(split_request[2], split_request[3])
		print(auth)
		if len(auth) > 0:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				s.connect(('127.0.0.1', 8000))
				s.sendall(request)
				response = s.recv(2048)
		else:
			response = 'Não autenticado'	
		balancer.sendall(str(response).encode())
		balancer.close()