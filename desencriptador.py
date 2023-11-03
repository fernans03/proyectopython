from cryptography.fernet import Fernet

# Cargar la clave de cifrado desde el archivo
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Desencriptar el archivo de contraseñas
with open("passwords.encrypted", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_data = cipher_suite.decrypt(encrypted_data)

# Mostrar las contraseñas
passwords = decrypted_data.decode().split("\n")[:-1]  # Dividir por líneas y eliminar la última línea en blanco

for i, password in enumerate(passwords, start=1):
    print(f"Contraseña {i}: {password}")
