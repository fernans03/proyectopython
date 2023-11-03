# Generador de Contraseñas Seguras y Almacenamiento en Archivo Encriptado

## Descripción
Este proyecto se centra en la generación de contraseñas seguras y su posterior almacenamiento en un archivo encriptado. Proporciona una forma de generar contraseñas fuertes y almacenarlas de manera segura.

## Características Principales
- Generación de contraseñas seguras con caracteres aleatorios.
- Almacenamiento de contraseñas en un archivo de texto.
- Encriptación del archivo de contraseñas para mayor seguridad.

## Requisitos
Asegúrate de tener instalados los siguientes requisitos antes de ejecutar el proyecto:
- Python 3.12
- Biblioteca cryptography (puedes instalarla con `pip install cryptography`)

## Instrucciones de Uso
1. Ejecuta el archivo `proyecto.py` para generar contraseñas seguras y encriptar las contraseñas.
2. Las contraseñas generadas se guardarán en un archivo llamado `passwords.txt`.
4. El archivo encriptado resultante se llamará `passwords.encrypted`.
5. Asegúrate de guardar de forma segura la clave de cifrado para futuras operaciones de desencriptado.

## Estructura del Proyecto
- `proyecto.py`: Código para generar contraseñas seguras y que encripta las contraseñas.
- `passwords.txt`: Archivo que almacena contraseñas generadas.
- `passwords.encrypted`: Archivo encriptado que almacena las contraseñas.
- `desencriptador.py` : Desencripta el archivo de contraseñas encriptadas.


