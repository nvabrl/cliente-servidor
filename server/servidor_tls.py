
import socket
import ssl

HOST = "0.0.0.0"
PUERTO = 5050

# Configuramos TLS para el servidor.
contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# Cargamos el certificado y la clave privada del servidor.
contexto.load_cert_chain(
    certfile="pki/servidor.crt",
    keyfile="pki/servidor.key"
)

# Creamos el servidor TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PUERTO))
    servidor.listen()

    print(f"Servidor TLS escuchando en {HOST}:{PUERTO}")
    print("Esperando conexiones...")

    while True:
        conexion, direccion = servidor.accept()
        print(f"\nConexión recibida desde {direccion}")

        try:
            # Convertimos la conexión TCP en una conexión TLS.
            with contexto.wrap_socket(
                conexion,
                server_side=True
            ) as conexion_segura:

                print("Conexión TLS establecida")
                print(f"Versión TLS: {conexion_segura.version()}")
                print(
                    f"Cifrado: {conexion_segura.cipher()[0]}"
                )

                mensaje = conexion_segura.recv(1024)

                if not mensaje:
                    print("El cliente cerró la conexión sin enviar datos.")
                    continue

                mensaje = mensaje.decode("utf-8")
                print(f"Mensaje recibido: {mensaje}")

                respuesta = "Mensaje recibido mediante TLS"
                conexion_segura.sendall(
                    respuesta.encode("utf-8")
                )

                print("Respuesta enviada al cliente.")

        except ssl.SSLError as error:
            print(f"Error TLS: {error}")

        except OSError as error:
            print(f"Error de conexión: {error}")

        finally:
            print("Conexión finalizada.")

