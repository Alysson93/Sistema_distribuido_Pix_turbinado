'''
	Atenção:
	Este arquivo deve ser executado apenas em dois cenários:
	1. Ao clonar o repositório;
	2. Ao apagar o banco de dados.
'''

import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS users(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		password TEXT NOT NULL,
		balance INTEGER,
		pixkey TEXT
	);
''')

cursor.execute('''
	INSERT INTO users (name, password, balance, pixkey)
	VALUES ('usuario1', 'senha1', 100, 'chave1'),
	('usuario2', 'senha2', 100, 'chave2'),
	('usuario3', 'senha3', 100, 'chave3'),
	('usuario4', 'senha4', 100, 'chave4'),
	('usuario5', 'senha5', 100, 'chave5'),
	('usuario6', 'senha6', 100, 'chave6'),
	('usuario7', 'senha7', 100, 'chave7'),
	('usuario8', 'senha8', 100, 'chave8'),
	('usuario9', 'senha9', 100, 'chave9'),
	('usuario0', 'senha0', 100, 'chave0');
''')
conn.commit()

conn.close()