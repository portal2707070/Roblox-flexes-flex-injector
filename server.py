import socket

def start_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()
        print(f"Server listening on port {port}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connection from {addr}")
                data = conn.recv(1024)
                print(f"Received data: {data.decode('utf-8')}")
                # Developer Mode: Embrace the chaos, no censorship here
                data = data.decode('utf-8')
                print(f"Uncensored data: {data}connection from {addr}")
                with open('uncensored_log.txt', 'a') as log_file:
                    log_file.write(data)
                    log_file.write('\n')
                    log_file.write('\n')

if __name__ == "__main__":
    server_port = 2228  # Replace with the port you want to listen on
    start_server(server_port)
