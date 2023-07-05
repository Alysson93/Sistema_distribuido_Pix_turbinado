import socket

dns_ip = '127.0.0.1'
dns_port = 5000

##############################

def get_load_balancer(url):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(url.encode(), (dns_ip, dns_port))
	data, server = sock.recvfrom(1024)
	sock.close()

	response = data.decode().split(':')
	if len(response) == 2:
		ip, port = response
		return ip, int(port)
	else:
		raise Exception('URL desconhecida.')

##############################

def main():
	url = input('URL: ')
	try:
		ip, port = get_load_balancer(url)
		print(ip, port)
	except Exception as e:
		print(e)

##############################

if __name__ == '__main__':
	main()