import socket
import threading

ip = '127.0.0.1'
port = 6000

sockets = [
	('127.0.0.1', 7000),
	('127.0.0.1', 7001)
]

##############################

def handle_request(client):
	current_computer = 0
	request = client.recv(2048).decode()
	try:
		current = sockets[current_computer]
		current_computer = (current_computer + 1) % len(sockets)
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend:
			backend.connect((current[0], current[1]))
			backend.sendall(request.encode())
			response = backend.recv(2048)
	except Exception as e:
		response = str(e).encode()
	client.sendall(response)
	client.close()

##############################

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip, port))
	sock.listen()
	print(f'Load balancer is running on {ip}:{port}')

	while True:
		client, _  = sock.accept()
		thread = threading.Thread(target=handle_request, args=(client,))
		thread.start()


##############################

if __name__ == '__main__':
	main()