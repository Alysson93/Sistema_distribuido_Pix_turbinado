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
	('usuario2', 'senha2', 100, 'chave2');
''')
conn.commit()

conn.close()