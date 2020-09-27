import sys, socket, argparse

HOST = '127.0.0.1'
SERVER_PORT = 8080

def client(host, port):

  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  except:
    print('Simplex-talk: socket')
    sys.exit(1)

  try:
    sock.connect((host, port))
  except:
    print('Simplex-talk: connect')
    sys.exit(1)

  print('Client has been assigned to', sock.getsockname())
  print('Type message to be sent to the server: ')

  message = None
  while True:
    message = input()
    if message == 'exit()':
      break
    sock.sendall(message.encode('ascii'))

  sock.close()

def main():
	parser = argparse.ArgumentParser(description='TCP Client')
	parser.add_argument('-port', type=int, default=SERVER_PORT, help='TCP port (default 8080)')
	parser.add_argument('-host', type=str, default=HOST, help='TCP host (default 127.0.0.1)')

	args = parser.parse_args()
	client(args.host, args.port)

if __name__ == '__main__':
  main()
