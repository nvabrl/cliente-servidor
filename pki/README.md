# Infraestructura de Clave Pública (PKI)

## Objetivo

Este módulo contiene los archivos necesarios para establecer una comunicación segura mediante TLS entre un cliente y un servidor.

## Archivos

- `ca.crt`: certificado público de la Autoridad Certificadora (CA), utilizado por el cliente para verificar el certificado del servidor.
- `servidor.crt`: certificado digital del servidor, que permite identificarlo durante el establecimiento de la conexión TLS.
- `servidor.ext`: archivo de extensiones utilizado durante la generación del certificado del servidor.

La clave privada `servidor.key` debe permanecer en el equipo donde se ejecuta el servidor y **no debe subirse a GitHub**.

## Verificación del certificado

Desde la carpeta raíz del repositorio, ejecutar:

```bash
openssl verify -CAfile pki/ca.crt pki/servidor.crt
```

Si el certificado es válido y está firmado por la CA indicada, el resultado esperado es:

```text
pki/servidor.crt: OK
```

## Consideraciones de seguridad

- La clave privada de la CA debe mantenerse protegida.
- No se deben compartir ni publicar claves privadas.
- El cliente TLS debe confiar en `ca.crt` para validar la identidad del servidor.
- Los certificados deben estar vigentes y contener los nombres o direcciones IP utilizados durante la conexión.