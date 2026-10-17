# Cliente TCP y TLS

## Objetivo

Este módulo contiene dos clientes para probar la comunicación con el servidor y comparar una conexión TCP sin cifrado con una conexión protegida mediante TLS.

## Archivos

- `cliente.py`: cliente TCP básico, sin cifrado TLS.
- `cliente_tls.py`: cliente que establece una conexión TLS y valida el certificado del servidor mediante la Autoridad Certificadora (CA).

## Requisitos

- Python 3 instalado.
- Servidor correspondiente iniciado en el puerto `5050`.
- Certificado de la CA disponible en `pki/ca.crt` para las conexiones TLS.

## Ejecución

Los comandos deben ejecutarse desde la carpeta raíz del repositorio.

### Cliente TCP sin cifrado

Con el servidor TCP iniciado en otra terminal:

```bash
python client/cliente.py
```

### Cliente TLS

Con el servidor TLS iniciado en otra terminal:

```bash
python client/cliente_tls.py
```

El cliente TLS valida el certificado del servidor utilizando `pki/ca.crt`. Si la validación tiene éxito, muestra la versión TLS y el cifrado negociado, envía un mensaje y recibe la respuesta del servidor.

## Consideraciones de seguridad

- La validación del certificado permite comprobar la confianza en la CA y la identidad del servidor.
- La dirección IP o el nombre utilizado por el cliente debe coincidir con uno de los nombres o direcciones IP incluidos en el certificado.
- No se debe desactivar la validación del certificado para evitar errores de conexión.
