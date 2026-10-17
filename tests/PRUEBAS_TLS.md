# Registro de pruebas de seguridad TLS

## 1. Objetivo

Comprobar que la comunicación entre el cliente y el servidor puede protegerse mediante TLS, que el cliente verifica la identidad del servidor y que se rechazan certificados que no cumplen las condiciones de confianza.

## 2. Pruebas realizadas

| Prueba | Resultado esperado | Resultado obtenido |
|---|---|---|
| Conexión TLS válida | Establecer una conexión segura e intercambiar mensajes | Aprobada |
| Negociación del protocolo | Utilizar una versión TLS compatible | TLS 1.3 |
| Negociación del cifrado | Seleccionar un conjunto de cifrado compatible | TLS_AES_256_GCM_SHA384 |
| Certificado firmado por la CA confiable | Aceptar el certificado del servidor | Aprobada |
| Certificado firmado por una CA no confiable | Rechazar la conexión | Rechazada correctamente |
| Nombre del servidor incorrecto | Rechazar la conexión por discrepancia de identidad | Rechazada correctamente |
| Conexión desde otra computadora | Intercambiar mensajes a través de la red local con TLS | Pendiente |

## 3. Evidencia de la conexión válida

El cliente mostró los siguientes resultados:

- Conexión TLS establecida.
- Versión TLS: TLSv1.3.
- Cifrado negociado: TLS_AES_256_GCM_SHA384.
- Respuesta del servidor: Mensaje recibido mediante TLS.

## 4. Pruebas negativas

### Certificado de una CA no confiable

Se configuró temporalmente el cliente para confiar en un certificado de una autoridad certificadora diferente. La validación falló con un error de certificado no confiable.

Después de la prueba, se restauró la configuración legítima del cliente.

### Nombre del servidor incorrecto

Se modificó temporalmente el nombre utilizado para verificar la identidad del servidor. La conexión fue rechazada porque el nombre no coincidía con los nombres incluidos en el certificado.

Después de la prueba, se restauró la configuración legítima del cliente.

## 5. Estado de la implementación

La conexión TLS local y las pruebas negativas se completaron correctamente. La conexión desde otro equipo queda pendiente de realizarse.

## 6. Observación

La conexión TLS proporciona cifrado e integridad durante la comunicación, mientras que la validación del certificado permite comprobar la identidad del servidor según la CA confiable y el nombre esperado. Estas propiedades no sustituyen los controles de autenticación y autorización de usuarios.

## 7. Prueba de recuperación ante una conexión fallida

**Procedimiento:**

1. Se inició el servidor TLS.
2. Se estableció una conexión legítima y se intercambiaron mensajes correctamente.
3. Se abrió una conexión TCP que se cerró sin completar la negociación TLS.
4. El servidor registró el error `UNEXPECTED_EOF_WHILE_READING`.
5. Sin reiniciar el servidor, se estableció una nueva conexión TLS válida.

**Resultado:** Aprobado. El servidor continuó atendiendo conexiones después del intento fallido.

**Conclusión:** El manejo de errores permite que el servidor continúe funcionando después de este tipo de fallo de conexión. Esta prueba no demuestra resistencia frente a todos los errores o ataques posibles.