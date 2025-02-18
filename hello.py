  GNU nano 8.3                                               hello.py                                               Modified





#!/usr/bin/env python3
import hashlib

mensaje = "Hola Mundo"
hash_object = hashlib.sha256(mensaje.encode('utf-8'))
hash_hex = hash_object.hexdigest()

print("El hash SHA256 de 'Hola Mundo' es:")
print(hash_hex)


