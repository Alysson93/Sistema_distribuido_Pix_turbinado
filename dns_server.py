import socket

domain_mappings = {
	'exemplo.com': ('127.0.0.1', 8080),
	'teste.com': ('127.0.0.1', 8081),
}

ip = '127.0.0.1'
port = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))


print(f'DNS server is running on {ip}:{port}')

while True:
	data, client = sock.recvfrom(1024)
	url = data.decode()

	if url in domain_mappings:
		address = domain_mappings[url]
		response = f'{address[0]}:{address[1]}'
	else:
		response = 'no url'

	
	sock.sendto(response.encode(), client)