import socketserver

class BotHandler(socketserver.BaseRequestHandler):

	commands = []
	
	#read the commands from the file and store them in the list
	@classmethod
	def load_commands(cls, filename):
		with open(filename, 'r') as f:
		#each instance should have access to the commands - hence cls
			cls.commands = [line.strip() for line in f]
	
	#recieves data from the client and sends out the commands
	def handle(self):
		self.data = self.request.recv(1024).strip()
		print("Bot with IP {} sent:".format(self.client_address[0]))
		print(self.data)
		
		for cmd in self.commands:
			self.request.sendall((cmd + "\n").encode())
		
if __name__ == "__main__":
	HOST, PORT = "", 8000
	
	BotHandler.load_commands('commands.txt')
	
	tcpServer = socketserver.TCPServer((HOST, PORT), BotHandler)
	try:
		tcpServer.serve_forever()
	except Exception as e:
		print("There was an error:". e)
