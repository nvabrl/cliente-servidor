
import socket

HOST = "127.0.0.1"
PUERTO = 5050

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PUERTO))

mensaje = "Hola, servidor. Soy el cliente."
cliente.sendall(mensaje.encode("utf-8"))

respuesta = cliente.recv(1024).decode("utf-8")
print(f"Respuesta del servidor: {respuesta}")

cliente.close()
