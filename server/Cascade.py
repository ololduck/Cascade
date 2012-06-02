#!/usr/bin/env python

import socket



class CascadeServer:
	"""Main Cascade Server class. Handles the file upload, and adding it to btcli"""
	def __init__(self, port):
		self.port = port
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def serve_forever(self):
		"""Launches the server: SERVE FOREVER"""
		self.configure()
		self.mainloop()

	def configure(self):
		self.s.bind(('',self.port))
		self.s.listen(1)

	def mainloop(self):
		while True:
			# client receptionning loop
			conn, addr = self.s.accept()
			while True:
				data = conn.recv(1024)
				if not data:
					break
				if data[0:2] == "PUT":
					conn.send("200 OK Proceed to file upload")
					file_length = data.split(' ')[2]
					torrent = conn.recv(file_length)