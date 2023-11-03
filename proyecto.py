import secrets
import string
from cryptography.fernet import Fernet

# Función para generar una contraseña segura
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += "!@#$%^&*()_-+=<>,.?/|"

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Solicitar al usuario las opciones de caracteres
length = int(input("Ingrese la longitud de la contraseña: "))
use_uppercase = input("¿Incluir mayúsculas? (S/N): ").strip().lower() == "s"
use_lowercase = input("¿Incluir minúsculas? (S/N): ").strip().lower() == "s"
use_digits = input("¿Incluir números? (S/N): ").strip().lower() == "s"
use_special_chars = input("¿Incluir caracte12res especiales? (S/N): ").strip().lower() == "s"

# Generar una lista de contraseñas seguras
passwords = [generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars) for _ in range(10)]

# Guardar las contraseñas en un archivo
with open("passwords.txt", "w") as file:
    for password in passwords:
        file.write(password + "\n")

# Generar una nueva clave para cifrar y guardarla en un archivo
key = Fernet.generate_key()
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

cipher_suite = Fernet(key)

# Encriptar el archivo de contraseñas
with open("passwords.txt", "rb") as file:
    data = file.read()

encrypted_data = cipher_suite.encrypt(data)

with open("passwords.encrypted", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

print("Contraseñas generadas y archivo encriptado creado. La clave de cifrado se ha guardado en 'encryption_key.key'.")
