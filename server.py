import socket
import threading
import os
from Database import Database

ip = '127.0.0.1'
port = 8000
db = Database()

mutex = threading.Lock()

def handle_request(client):
	request = client.recv(2048).decode()
	pid, _, user, password, option, pixkey, value = request.split('|')
	response = ''
	if option == '1':
		response = db.get_balance(user, password)
		response = str(response[0][0])
	elif option == '2':
		db.send_value(user, password, pixkey, value)
		response = 'Transferência realizada'
	mutex.acquire()
	client.sendall(response.encode())
	mutex.release()
	client.close()

##############################

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((ip, port))
	sock.listen(5)

	print(f'Server is running on {ip}:{port}')

	while True:
		client, addr = sock.accept()
		thread = threading.Thread(target=handle_request, args=(client,))
		thread.start()

##############################

if __name__ == '__main__':
	main()
