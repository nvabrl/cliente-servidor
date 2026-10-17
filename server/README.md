# Servidor TCP y TLS

## Objetivo

Este módulo implementa dos versiones de un servidor para comparar la comunicación TCP sin cifrado con la comunicación protegida mediante TLS.

## Archivos

- `servidor.py`: servidor TCP básico, sin cifrado TLS.
- `servidor_tls.py`: servidor que utiliza TLS para proteger la comunicación y presentar su certificado digital al cliente.

## Requisitos

- Python 3 instalado.
- Certificado del servidor: `pki/servidor.crt`.
- Clave privada correspondiente: `pki/servidor.key`.

La clave privada debe estar disponible localmente, pero nunca debe subirse al repositorio.

## Ejecución

Los comandos siguientes deben ejecutarse desde la carpeta raíz del repositorio.

### Servidor TCP sin cifrado

```bash
python server/servidor.py
```

### Servidor TLS

```bash
python server/servidor_tls.py
```

El servidor TLS escucha en el puerto `5050` y muestra información sobre la conexión, incluida la versión TLS y el cifrado negociado.

## Consideraciones

- El servidor utiliza el certificado ubicado en `pki/servidor.crt`.
- La clave privada correspondiente se encuentra en `pki/servidor.key`.
- El puerto `5050` debe estar disponible antes de iniciar el servidor.
- Para las pruebas desde otro equipo, el cliente debe utilizar la dirección IP correcta del servidor y el certificado debe incluir esa dirección en sus extensiones SAN.