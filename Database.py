import sqlite3

class Database:

	def __init__(self):
		self._path = 'database.db'


	def auth(self, user, password):
		conn = sqlite3.connect(self._path)
		cursor = conn.cursor()

		cursor.execute('''
			SELECT * FROM users
			WHERE name = ? AND password = ?
		''', (user, password))

		count = cursor.fetchall()
		conn.commit()
		conn.close()
		return count


	def get_balance(self, user, password):
		conn = sqlite3.connect(self._path)
		cursor = conn.cursor()

		cursor.execute('''
			SELECT balance FROM users
			WHERE name = ? AND password = ?
		''', (user, password))

		balance = cursor.fetchall()
		conn.commit()
		conn.close()
		return balance


	def send_value(self, user, password, pixkey, value):
		conn = sqlite3.connect(self._path)
		cursor = conn.cursor()

		cursor.execute('''
			UPDATE users
			SET balance = balance - ?
			WHERE name = ? AND password = ?
		''', (value, user, password))

		cursor.execute('''
			UPDATE users
			SET balance = balance + ?
			WHERE pixkey = ?
		''', (value, pixkey))

		balance = cursor.fetchall()
		conn.commit()
		conn.close()