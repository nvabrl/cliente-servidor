# Sistema de Comunicaciones Seguras Cliente-Servidor

Solución tecnológica integral que representa la infraestructura de comunicaciones seguras de una pequeña organización, demostrando el uso de distintos mecanismos de seguridad para proteger redes y sesiones por Internet.

---

##  Contexto y Objetivo
El proyecto implementa una arquitectura cliente-servidor para contrastar la comunicación abierta frente a entornos cifrados y protegidos. El propósito no es construir protocolos de producción, sino demostrar y comprobar los diferentes objetivos de cada mecanismo: proteger sesiones, validar identidades mediante certificados, administrar equipos de forma remota, aislar tráfico entre redes y controlar accesos privilegiados.

---

##  Módulos y Requerimientos del Sistema

1. **Comunicación Cliente-Servidor y TLS** — Aplicación cliente y servidor en computadoras diferentes, con comparativa directa entre tráfico sin protección y sesiones cifradas mediante TLS y certificados digitales.
2. **PKI y Cadena de Confianza** — Autoridad Certificadora (CA) generada mediante **OpenSSL** para emitir y validar la cadena de confianza, rechazando certificados no confiables.
3. **Administración mediante SSH** — Acceso administrativo seguro con autenticación de usuarios, restricción de acceso a personal autorizado y registro detallado de intentos de conexión.
4. **IPSec (Modos y Anti-Replay)** — Simulación a nivel de software de IPSec diferenciando entre **modo transporte** y **modo túnel**, incluyendo un mecanismo de protección contra ataques de *replay* (paquetes repetidos).
5. **VPN de Acceso Remoto** — Autenticación y acceso segmentado para usuarios remoting, asegurando que los recursos disponibles dependan estrictamente de los privilegios del usuario.
6. **VPN Sitio a Sitio** — Configuración para interconectar dos redes diferentes de manera aislada, diferenciándose claramente del acceso remoto.
7. **AAA (Autenticación, Autorización y Registro)** — Diferenciación clara entre validar identidad (autenticación) y otorgar permisos (autorización), respaldado por un sistema de *logging* para conexiones, accesos y operaciones administrativas.
8. **Pruebas de Seguridad** — Validación práctica del funcionamiento de TLS, rechazo de certificados inválidos, accesos SSH autorizados/denegados, modos IPSec, detección de *replay*, túneles VPN y restricciones de recursos.
9. **Documentación** — Arquitectura detallada, instrucciones de ejecución y limitaciones de seguridad documentadas en el proyecto.

---

##  Stack Tecnológico

| Componente | Tecnología |
| :--- | :--- |
| **Frontend / Cliente** | Python |
| **Backend / Servidor** | Python |
| **Criptografía / PKI** | OpenSSL, TLS 1.3 / 1.2 |
| **Redes y Simulación** | Sockets TCP/IP, OpenSSH, IPSec / VPN Simulation |

---

##  Estructura del Repositorio

```text
.
├── client/           # Aplicación cliente y cliente de prueba TLS/VPN
├── server/           # Aplicación servidor y validación de conexiones seguras
├── pki/              # Autoridad Certificadora (CA), llaves y certificados OpenSSL
├── ssh/              # Módulo de administración SSH y bitácoras de registro
├── ipsec/            # Simulación de modo transporte, túnel y anti-replay
├── vpn/              # Configuración de VPN de acceso remoto y sitio a sitio
├── tests/            # Scripts de pruebas de seguridad y validación
└── README.md         # Documentación técnica completa del proyecto
```

---

## Equipo de Trabajo

| Integrante | Matrícula |
| :--- | :--- |
| **Gerardo Alexis Hinojos Snachez** | `238999`  |
| **Abril Márquez De la O** | `238488` |
| **Bruno Castro Nuñez** | `215048` |


**Materia:** Seguridad de la información II  
**Institución:** Universidad Autónoma de Ciudad Juárez — CU

---

## ⚙️ Instrucciones de Ejecución
Consulta el [README.md](README.md) individual de cada carpeta (`/pki`, `/server`, `/client`) para conocer los comandos específicos de inicialización de la Autoridad Certificadora, levantamiento del servidor TLS y ejecución de las pruebas de seguridad.

---

## 📜 Licencia / Uso
Proyecto académico desarrollado para fines educativos. Uso restringido en el marco de las actividades de la materia.
