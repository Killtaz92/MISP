import hashlib

# Ruta del archivo .py que deseas cifrar
archivo_path = 'EJECRICIO.py'

# Mostrar "Hola Mundo"
print("Hola Mundo")

# Abrir el archivo en modo binario
with open(archivo_path, 'rb') as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read()

    # Crear el objeto hash SHA-256
    sha256_hash = hashlib.sha256()

    # Actualizar el hash con el contenido del archivo
    sha256_hash.update(contenido)

    # Obtener el hash final en formato hexadecimal
    hash_hex = sha256_hash.hexdigest()

    # Mostrar el hash
    print(f'El hash SHA-256 del archivo es: {hash_hex}')
