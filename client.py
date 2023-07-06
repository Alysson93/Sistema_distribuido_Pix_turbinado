import socket
import os

pid = str(os.getpid())

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

def send_to_load_balancer(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, port))
	user = input('Usuário: ')
	password = input('Senha: ')
	print('Que operação você deseja realizar?')
	print('1 - Imprimir saldo')
	print('2 - Fazer transferência')
	option = input('Digite sua opção aqui: ')
	pixkey = input('Chave destino: ') if option == '2' else '0'
	value = float(input('Valor a ser transferido: ')) if option == '2' else '0'
	message = f'{pid}|1|{user}|{password}|{option}|{pixkey}|{value}'
	sock.sendall(message.encode())
	response = sock.recv(2048).decode()
	sock.close()
	return response


##############################

def main():
	url = input('URL: ')
	try:
		ip, port = get_load_balancer(url)
		response = send_to_load_balancer(ip, port)
		print(response)
	except Exception as e:
		print(e)

##############################

if __name__ == '__main__':
	main()