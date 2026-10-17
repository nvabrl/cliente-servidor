
import socket
import ssl

HOST = "192.168.0.85"
PUERTO = 5050

# Creamos un contexto TLS que verifica certificados.
contexto = ssl.create_default_context(
    cafile="pki/ca.crt"
)

with socket.create_connection((HOST, PUERTO)) as cliente:
    # Establecemos TLS y verificamos la identidad del servidor.
    with contexto.wrap_socket(
        cliente,
        server_hostname="192.168.0.85"
    ) as conexion_segura:

        print("Conexión TLS establecida")
        print(f"Versión TLS: {conexion_segura.version()}")
        print(f"Cifrado negociado: {conexion_segura.cipher()[0]}")

        mensaje = "Hola, servidor. Soy el cliente TLS."
        conexion_segura.sendall(mensaje.encode("utf-8"))

        respuesta = conexion_segura.recv(1024).decode("utf-8")
        print(f"Respuesta del servidor: {respuesta}")
