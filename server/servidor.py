
import socket

HOST = "127.0.0.1"
PUERTO = 5050

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PUERTO))
servidor.listen()

print(f"Servidor escuchando en {HOST}:{PUERTO}")

conexion, direccion = servidor.accept()
print(f"Cliente conectado desde {direccion}")

mensaje = conexion.recv(1024).decode("utf-8")
print(f"Mensaje recibido: {mensaje}")

conexion.sendall("Mensaje recibido correctamente".encode("utf-8"))

conexion.close()
servidor.close()
