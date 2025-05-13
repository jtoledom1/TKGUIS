# logica/procesador.py

import hashlib

def leer_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error al leer archivo: {e}"

def encriptar(texto, metodo):
    if metodo == "SHA256":
        return hashlib.sha256(texto.encode()).hexdigest()
    elif metodo == "AES":
        return "🔐 Simulación de AES (aún sin implementar)"
    elif metodo == "RSA":
        return "🔐 Simulación de RSA (aún sin implementar)"
    else:
        return "Método de encriptación no reconocido"
