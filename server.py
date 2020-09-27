import sys, socket, argparse

HOST = '127.0.0.1'
SERVER_PORT = 8080
MAX_LINE = 256
MAX_PENDING = 5

def recvAll(conn):
  data = b''
    
  while len(data) < MAX_LINE:
    data_received = conn.recv(MAX_LINE - len(data))
    if not data_received:
        conn.close()
        return None
    
    print(data_received.decode('ascii'))
    data += data_received
  
  return data

def server(interface, port):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  except:
    print('Simplex-talk: socket')
    sys.exit(1)
    
  try: 
    sock.bind((interface, port))
  except:
    print('Simplex-talk: bind')
    sys.exit(1)
  
  sock.listen(MAX_PENDING)
    
  print('Server listening at', sock.getsockname())

  while True:
    try:
      conn, address = sock.accept()
    except:
      print('Simplex-talk: accept')
      sys.exit(1)
    
    print('Estabilished connection with address', address)

    message = recvAll(conn)
    if message != None:
      print("Message sent:", message.decode('ascii'))
    
    conn.close()

def main():
  parser = argparse.ArgumentParser(description='TCP Server')
  parser.add_argument('-port', type=int, default=SERVER_PORT, help='TCP port (default 8080)')
  parser.add_argument('-host', type=str, default=HOST, help='TCP host (default 127.0.0.1)')
  
  args = parser.parse_args()
  server(args.host, args.port)

if __name__ == '__main__':
  main()

