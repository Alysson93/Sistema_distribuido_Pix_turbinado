import sqlite3
import threading

class Database:

	def __init__(self):
		self._path = 'database.db'
		self._lock = threading.Lock()


	def auth(self, user, password):
		self._lock.acquire()
		try:
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

		finally:
			self._lock.release()
